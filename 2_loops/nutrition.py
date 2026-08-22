# fruits_dict = {"apple": 130, "avocado": 50, "banana": 110}

# user_ask = input("Item: ").lower()

# if user_ask in fruits_dict:
#     print("Calories:", fruits_dict[user_ask])


def any_fruits(user_ask ):
    fruits_dict = {"apple": 130, "avocado": 50, "banana": 110}
    # user_ask = input("Item: ").lower()

    if user_ask in fruits_dict:
        return fruits_dict[user_ask]
    return "Item not found in the dictionary."

def main():
    print(any_fruits(input("Item: ").lower()))

if __name__ == "__main__":
    main()