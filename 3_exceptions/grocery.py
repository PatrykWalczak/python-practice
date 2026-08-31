counts = {}
while True:
    try:
        user_input = input().upper()
        if user_input in counts:
            counts[user_input] += 1
        else:
            counts[user_input] = 1

    except EOFError:
        for i in sorted(counts):
            print(f"{counts[i]} {i}")
        break
    