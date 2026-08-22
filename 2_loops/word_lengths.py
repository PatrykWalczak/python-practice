def lengths(words):
    empty_dict = {}
    for word in words:
        empty_dict[word] = len(word)
    return empty_dict

def main():
    print(lengths(["cat", "monkey", "elephant"]))

if __name__ == "__main__":
    main()