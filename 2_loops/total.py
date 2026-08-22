def total(numbers1, numbers2):
    total_sum1 = 0
    total_sum2 = 0
    for number in numbers1:
        total_sum1 += number
    for number in numbers2:
        total_sum2 += number
    return total_sum1, total_sum2


def main():
    print(total([10, 20, 30], [5, 5]))

if __name__ == "__main__":
    main()