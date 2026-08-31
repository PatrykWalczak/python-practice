menu_prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



total_cost = 0
while True:
    try:
        user_order = input("Item: ").title()
        if user_order in menu_prices:
            total_cost += menu_prices[user_order]
            print(f"Total: ${total_cost:.2f}")
        else:
            continue
    except EOFError:
        print("Zatrzymałeś program")
        break
    except KeyboardInterrupt:
        print("Inny sposb zatrzymania")
        break