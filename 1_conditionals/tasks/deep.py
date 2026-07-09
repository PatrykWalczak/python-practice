def answer():
    user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    user = user.lower().strip()
    return "Yes" if user == str(42) or user == "forty-two" or user == "forty two" else "No"

def main():
    print(answer())

main()