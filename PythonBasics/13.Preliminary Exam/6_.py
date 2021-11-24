n = int(input())
found = False
counter = 0

for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                # sum_numbers = a + b + c + d
                # numbers_multiplied = a * b * c * d
                if (a + b + c + d) == a * b * c * d and n % 10 == 5:
                    counter += 1
                    print(f'{a}{b}{c}{d}')
                    found = True
                    break
                elif a * b * c * d  // (a+b+c+d) == 3 and n % 3 == 0:
                    counter += 1
                    print(f'{d}{c}{b}{a}')
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break
if counter == 0:
    print("Nothing found")

#killed it. 