from pymongo import MongoClient
from abc import ABC
from app.Data.db.settings import *


client = MongoClient(f'mongodb://{HOST}:{PORT}')
db = client.tard1s


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()
        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return self.__dict__['name']

    def save(self):
        if not self._id:
            del(self.__dict__['_id'])
            return self.collection.insert_one(self.__dict__)
        else:
            return self.collection.update({'_id': self._id}, self.__dict__)

    def remove_field(self, field):
        self.collection.update({'_id': self._id}, {"$unset": {field: ""}})

    @classmethod
    def add(cls, item):
        cls(item).save()

    @classmethod
    def add_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))

    def insert_into_array(self, field_name, new_value):
        self.collection.update_one({'_id': self._id}, {'$push': {field_name: new_value.to_dict()}})

    def remove_from_array(self, field_name, value):
        self.collection.update_one({'_id': self._id}, {'$pull': {field_name: value.to_dict()}})

    def update_field(self, field_name, new_value):
        self.collection.update_one({'_id': self._id}, {'$set': {field_name: new_value.to_dict()}})

    @classmethod
    def remove(cls, **kwargs):
        cls.collection.delete_many(kwargs)


class EmbeddedDocument(dict, ABC):
    repr_data = None

    def __init__(self, data):
        super().__init__()
        self.__dict__.update(data)

    def __repr__(self):
        return self.__dict__[self.repr_data]

    def to_dict(self):
        return self.__dict__

