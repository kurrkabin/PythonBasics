number = int(input())
current = 1
current_bigger_than_n = False
for x in range(1, number + 1):
    for y in range(1, x + 1):
        print(current, end = ' ')
        current += 1
        if current> number:
            current_bigger_than_n = True
            break
    if current_bigger_than_n:
        break
    print()