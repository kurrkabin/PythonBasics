number = int(input()) #брой на числата, които въвъждаме. Например 2, означава, че ще вкараме 2 нови числа, които да се съберат

total_sum = 0
for _ in range(number): # с долната черта показваме, че не ни интересува променливатата (не знаем колко числа ще въртим)
    # и затова слагаме _, нещо като pass в if construction
    current_num = int(input()) # вземаме числата от тук, т.е. това са тези 2 числа, например 10 и 20
    total_sum += current_num #тук имаме сбора на тези две числа, т.е. 10+20 - 30

print(total_sum)

# Judge approved. Second option is this:
#
# number = int(input())
# total_sum = 0

# for x in range(number):
#     current_num = int(input())
#     total_sum += current_num
#
# print(total_sum)