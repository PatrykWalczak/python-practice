# def count_long_words(words):
#     letter_count = 0
#     for word in words:
#         if len(word) > 5:
#             letter_count += 1
#     return letter_count



# def main():
#     print(count_long_words(["hello", "world", "python", "is", "greataaa"]))

# if __name__ == "__main__":
#     main()


# user = input("Podaj słowa do sprawdzenia: ")
# words = user.split()
# letter_count = 0
# more_then_five = []
# for word in words:
#     if len(word) > 5:
#         letter_count += 1
#         more_then_five.append(word)
# print(f'Mamy tylko {letter_count} słów dłuższych niż 5 liter. Tylko słowami są:{more_then_five}')

def count_long_words(words):
    letter_count = 0
    more_then_five = []
    for word in words:
        if len(word) > 5:
            letter_count += 1
            more_then_five.append(word)
    return letter_count, more_then_five

def main():
    user = input("Podaj slowa do sprawdzenia:")
    user = user.replace(",", " ")
    words = user.split()
    print(count_long_words(words))

if __name__ == "__main__":
    main()


