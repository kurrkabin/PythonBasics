# num = int(input())
#
# even_sum = 0
# odd_sum = 0
#
# for x in range(num):
#     current_number = int(input())
#
#     if x % 2 == 0:
#         even_sum += current_number
#     else:
#         odd_sum += current_number
#
# if odd_sum == even_sum:
#     print('Yes')
#     print(f'Sum = {even_sum}')
#
# else:
#     diff = abs(odd_sum - even_sum)
#     print('No')
#     print(f'Diff = {diff}')

num = int(input())
sum = 0

for x in range(num):
    current_number = int(input())
    sum += current_number

print(sum)
