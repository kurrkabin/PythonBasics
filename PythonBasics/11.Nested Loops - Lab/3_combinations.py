number = int(input())
combinations = 0
result = 0


for x in range(number+1):
    for y in range (number+1):
        for z in range(number+1):
            result = x+y+z
            if result == number:
                combinations+=1
print(combinations)

