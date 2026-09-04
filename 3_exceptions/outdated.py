months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

months_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}




while True:
    ask_user = input("Date: ")
    try:
        if "/" in ask_user:
            splited_list = ask_user.split("/")
            month = int(splited_list[0])
            day = int(splited_list[1])
            year = int(splited_list[2])


            if 1 <= month <= 12 and 1 <= day <= 31:
                day = f"{day:02d}"
                month = f"{month:02d}"
                number_data = f"{year}-{month}-{day}"
                print(number_data)
                break
            else:
                raise ValueError()
    except ValueError:
        print("ValueError- mozliwe problemy to: STR zamiast INT, nieprawidłowy dzień / miesiąć ")





