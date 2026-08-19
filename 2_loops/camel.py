def user_question(user):
    snake_case = ""
    for letter in user:
        if letter.isupper():
            snake_case += "_" + letter.lower()
        else:
            snake_case += letter
    return snake_case

def main():
    print(user_question(input("snakeCase: ")))

main()



