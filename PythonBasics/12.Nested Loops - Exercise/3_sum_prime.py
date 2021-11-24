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

