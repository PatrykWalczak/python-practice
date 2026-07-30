def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if 18.5 > bmi:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    user_weight = input("Podaj swoją wagę w kg:")
    user_height = input("Podaj swój wzrost w metrach:")
    user_weight, user_height = float(user_weight), float(user_height)
    user_bmi = calculate_bmi(user_weight, user_height)
    print(f"BMI: {user_bmi:.1f}, Kategoria: {classify_bmi(user_bmi)}")

if __name__ == "__main__":
    main()
    