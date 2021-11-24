

#trick is to include the 2 in the total calculations
n = int(input())
for x in range(n + 1):
    if x % 2 == 0:
        print(2 ** x)
