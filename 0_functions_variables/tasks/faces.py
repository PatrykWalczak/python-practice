def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    result = convert(input("Ask: "))
    print(result)
main()
