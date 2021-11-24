first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)
    if odd_digits_sum == even_digits_sum:
        print(current_number_as_string, end=' ')

#end = ' ', it gave me 100%

#Notes:
#1.if you place odd_digit_sum and even_digit_sum outside the for-loop, it calculates the odd/even sum for overall w/o resetting for each new number, this way
# you just see the end result of the sum of all odd vs even numbers. Instead, the sum should reset with each new current number.

#2.Why do we need to have the last "if odd_digit_sum == even_digit_sum outside the inner loop, but inside the first loop?
#-If we leave it inside the inner circle, it will print a number the moment it equalizes even if there are more digits to come. If it stays outside the inner circle, it
#only does it when the number is complete.

