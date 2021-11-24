number = int(input())
magic_number = True

for magic_number in range(1111,9999+1):
    string_magic = str(magic_number)
    for digit in string_magic:
        int_digit = int(digit)
        if int_digit== 0 or number % int_digit!=0:
            magic_number= False
            break
    if magic_number:
        print(magic_number, end= ' ')


#Killed it. Reverse engineering. Used a boolean to make my life easier. Then moved the 'if magic_number' outside the
#nested loop so that it doesn't print things with each iteration
#Check line 22-25 to understand the original solution


# number = int(input())
# magic_number = True
#
# for magic_number in range(1111,9999+1):
#     string_magic = str(magic_number)
#     for index, digit in enumerate(string_magic):
#         int_digit = int(digit)
#         if int_digit== 0 or number % int_digit!=0:
#             magic_number= False
#             break
#     if magic_number:
#         print(magic_number, end= ' ')
#
#
#--------------------------------------------------------------------------------------------------------------------

# number = int(input())
# for current_number in range(1111,9999+1):
#     number_is_special = True
#     current_number_as_string = str(current_number)
#     for current_digit in current_number_as_string:
#         if int(current_digit) == 0 or number % int(current_digit) != 0:
#             number_is_special = False
#             break
#     if number_is_special:
#         print(current_number, end = ' ')

