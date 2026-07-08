def einstein_program(mass):
    return (mass * 300000000 ** 2)


def main():
    result = einstein_program(int(input("m: ")))
    print(result)

main()