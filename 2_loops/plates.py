def main():
    plate = str(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return starts_with_letters(s) and has_valid_length(s) and digits_only_at_end(s) and only_letters_and_digits(s)

def starts_with_letters(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    return False


def has_valid_length(s):
    if 2 <= len(s) <= 6:
        return True
    return False



def digits_only_at_end(s):
    digit_started = False
    for char in s:
        if digit_started and not char.isdigit():
            return False
        if char.isdigit():
            if not digit_started and char == "0":
                return False
            digit_started = True
    return True

def only_letters_and_digits(s):
    for char in s:
        if not char.isalnum():
            return False
    return True

main()