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
    total = sum-biggest  
    total1 = abs(biggest-total) 
    print('No')
    print(f'Diff = {total1}')


#Judge approved.

