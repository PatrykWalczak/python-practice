def main():
    user = convert(input("What time it is? "))
    if 7.0 <= user <= 8.0:
        print("breakfast time")
    elif 12.0 <= user <= 13.0:
        print("lunch time")
    elif 18.0 <= user <= 19.0:
        print("dinner time")
    

def convert(time):
    time = time.split(":")
    hh = int(time[0])
    mm = int(time[1]) / 60
    return hh + mm


if __name__ == "__main__":
    main()

# time = input("What time is it? ")
# time = time.split(":")
# hh = int(time[0])
# mm = int(time[1]) / 60
# print(hh + mm)

