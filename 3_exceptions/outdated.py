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


def parse_numeric(date_str):
    splited_list = date_str.split("/")
    month = int(splited_list[0])
    day = int(splited_list[1])
    year = int(splited_list[2])
    return month, day, year


def parse_worded(date_str):
    splited_list = date_str.replace(",", "").split()
    month = months_list.index(splited_list[0]) + 1
    day = int(splited_list[1])
    year = int(splited_list[2])
    return month, day, year


def format_date(month, day, year):
    if 1 <= month <= 12 and 1 <= day <= 31:
        day = f"{day:02d}"
        month = f"{month:02d}"
        number_data = f"{year}-{month}-{day}"
        return number_data
    else:
        raise ValueError()


def main():
    while True:
        ask_user = input("Date: ")
        try:
            if "/" in ask_user:
                month, day, year = parse_numeric(ask_user)
                answer = format_date(month, day, year)
                print(answer)
                break
            else:
                month, day, year = parse_worded(ask_user)
                answer = format_date(month, day, year)
                print(answer)
                break
        except ValueError:
            print("ValueError- mozliwe problemy to: STR zamiast INT, nieprawidłowy dzień / miesiąć ")


if __name__ == "__main__":
    main()



# while True:
#     ask_user = input("Date: ")
#     try:
#         if "/" in ask_user:
#             splited_list = ask_user.split("/")
#             month = int(splited_list[0])
#             day = int(splited_list[1])
#             year = int(splited_list[2])


#             if 1 <= month <= 12 and 1 <= day <= 31:
#                 day = f"{day:02d}"
#                 month = f"{month:02d}"
#                 number_data = f"{year}-{month}-{day}"
#                 print(number_data)
#                 break
#             else:
#                 raise ValueError()
            
#         else:
#             splited_list = ask_user.replace(",", "").split()
#             month = months_list.index(splited_list[0]) + 1
#             day = int(splited_list[1])
#             year = int(splited_list[2])

#             if 1 <= month <= 12 and 1 <= day <= 31:
#                 day = f"{day:02d}"
#                 month = f"{month:02d}"
#                 year = f"{year}-{month}-{day}"
#                 print(year)
#                 break
#             else:
#                 raise ValueError()
            
#     except ValueError:
#         print("ValueError- mozliwe problemy to: STR zamiast INT, nieprawidłowy dzień / miesiąć ")





