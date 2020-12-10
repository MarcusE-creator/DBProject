def int_input(user_input):
    while True:
        data = input(user_input)
        if data.isdigit():
            return int(data)
        else:
            print("Ditt svar måste vara ett heltal.")


def price_input(user_input):
    while True:
        data = input(user_input)
        try:
            return float(data)
        except ValueError:
            print("Ditt svar måste vara numeriskt.")

def print_title(title: str) -> None:
    padded_title = title.center(len(title) + 4)
    border = '-' * len(padded_title)
    print(padded_title)
    print(border)