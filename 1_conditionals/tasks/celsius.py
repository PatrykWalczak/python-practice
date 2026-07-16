def to_fahrenheit(celsius):
    celsius = float(celsius)
    celsius = (celsius * 9 / 5) + 32
    return celsius


def main():
    user_raw = float(input("Jaka to temperatura w Celcjuszach: "))
    user = to_fahrenheit(user_raw)
    print(f"{user_raw:.1f} C = {user:.1f} F")

if __name__ == "__main__":
    main()