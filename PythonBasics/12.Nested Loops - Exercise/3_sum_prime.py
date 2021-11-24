number = input()
sum_prime = 0
sum_non_prime = 0

while number != 'stop':
    current_number = int(number)
    if current_number < 0:
        print('Number is negative.')
    for x in range(2, current_number):
        if current_number % x == 0:
            sum_non_prime += current_number
            break
    if current_number >=0:
        sum_prime += current_number
    number = input()

sum_prime2 = sum_prime - sum_non_prime
print(f'Sum of all prime numbers is: {sum_prime2}')
print(f'Sum of all non prime numbers is: {sum_non_prime} ')

#Killed it. What I did it is: calculate the sum off all numbers. 2. Deduct non_prime from the sum of all numbers



# sum_of_prime_numbers = 0
# sum_of_none_prime_numbers = 0
# command = input()
# while command != 'stop':
#     current_number = int(command)
#     if current_number < 0:
#         print('Number is negative.')
#     else:
#         number_is_prime = True
#         for number in range(2, current_number):
#             if current_number % number == 0:
#                 number_is_prime = False
#                 break
#         if number_is_prime:
#             sum_of_prime_numbers += current_number
#         else:
#             sum_of_none_prime_numbers += current_number
#     command = input()
#
# print(f'Sum of all prime numbers is: {sum_of_prime_numbers}')
# print(f'Sum of all non prime numbers is: {sum_of_none_prime_numbers}')
#
#
