# user_list = {}
# user_list = ['a', 'b', 'c', 'd', 'e', 'b', 'd', 'd', 'c', 'e', 'c', 'c']
# most_common = []


# def most_common_function(user_list): 
#     counts = {}

#     for letter in user_list:
#         if letter in counts:
#             counts[letter] += 1
#         else:
#             counts[letter] = 1


#     most_common = ""
#     highest_common = 0
#     for x in counts:
#         if counts[x] > highest_common:
#             highest_common = counts[x]
#             most_common = x
#     return most_common


# def main():
#     print(most_common_function(['a', 'b', 'c', 'd', 'e', 'b', 'd', 'd', 'c', 'e', 'c', 'c']))


# main()

# funkcja która tworzy mi słownik 
def letter_dict(items):
    counts = {}

    for letter in items:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


# funkcja, która przyjmuje jako argument ten slownik
def find_most_common(counts_dict):
    most_common = ""
    highest_common = 0
    for x in counts_dict:
        if counts_dict[x] > highest_common:
            highest_common = counts_dict[x]
            most_common = x
    return most_common


def main():
    user_list = ['a', 'b', 'c', 'd', 'e', 'b', 'd', 'd', 'c', 'e', 'c', 'c']
    result_letter_dict = letter_dict(user_list)
    print(find_most_common(result_letter_dict))

main()


    