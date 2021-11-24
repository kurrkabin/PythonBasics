num = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(num):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number <=399:
        p2 += 1
    elif current_number <= 599:
        p3 += 1
    elif current_number <= 799:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

print1 = p1 / num * 100
print2 = p2 / num * 100
print3 = p3 / num * 100
print4 = p4 / num * 100
print5 = p5 / num * 100

print(f'{print1:.2f}%')
print(f'{print2:.2f}%')
print(f'{print3:.2f}%')
print(f'{print4:.2f}%')
print(f'{print5:.2f}%')

