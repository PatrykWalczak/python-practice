def area(width, height):
    return width * height


def perimeter(width, height):
    return 2 * (width + height)


def main():
    user_width = input("Podaj szerokość prostokąta: ")
    user_height = input("Podaj wysokośc prostokąta: ")
    user_width, user_height = float(user_width), float(user_height)
    area_result = area(user_width, user_height)
    perimeter_result = perimeter(user_width, user_height)
    print(f"Dla {user_width} i {user_height} pole wynosi: {area_result:.1f}, a obwód: {perimeter_result:.1f}")


if __name__ == "__main__":
    main()
