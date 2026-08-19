def skip_vowels(ask_user):
    new_word = ""
    for letter in ask_user:
        if letter.lower() in "aeiou":
            pass
        else:
            new_word += letter
    return new_word

   



def main():
    print(skip_vowels(str(input("Input: "))))

main()
