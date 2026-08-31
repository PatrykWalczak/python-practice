while True:
    try:
        ask_user = input("Fraction: ").split("/")
        user_x = int(ask_user[0])
        user_y = int(ask_user[1])
        if user_x > user_y:
            raise ValueError()
        percent = user_x / user_y * 100
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{round(percent)}")
        break
    
    except ValueError:
        print("Problem z x albo y - jedno z nich nie jest int")
    except ZeroDivisionError:
        print('Nie można dzielić przez zero')

