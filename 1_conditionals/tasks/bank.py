# bez funkcji 
# user = input("Greeting: ")
# user = user.lower().strip()

# if user.startswith("hello"):
#     print("$0")
# elif user.startswith("h"):
#     print("$20")
# else:
#     print("$100")

# funkcją 
def greeting_of():
    x = input("Greeting: ")
    x = x.lower().strip()
    if x.startswith("hello"):
        return "$0"
    elif x.startswith("h"):
        return "$20"
    else:
        return "$100"


def main():
    print(greeting_of())

main()