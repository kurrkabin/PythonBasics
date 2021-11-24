import sys

num = int(input())
sum = 0
biggest = -sys.maxsize

for i in range(num):
    current_number = int(input())
    sum += current_number
    if current_number > biggest:
        biggest = current_number

if biggest == sum - biggest:
    print('Yes')
    print(f'Sum = {biggest}')
else:
    total = sum-biggest  # 12 - 10 - така намираме сумата от другите числа
    total1 = abs(biggest-total) #10-2 - така вадим сумата на другите числа от най-голямото
    print('No')
    print(f'Diff = {total1}')


#Judge approved.

