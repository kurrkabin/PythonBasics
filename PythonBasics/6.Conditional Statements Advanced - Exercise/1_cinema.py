# screening = input()
# rows = int(input())
# columns = int(input())
# price_projection = 0
#
# if screening =='Premiere':
#     price_projection = 12
#     income = rows * columns * price_projection
#     print(f'{income:.2f}')
# elif screening == 'Normal':
#     price_projection = 7.5
#     income = rows * columns * price_projection
#     print(f'{income:.2f}')
# elif screening == 'Discount':
#     price_projection = 5
#     income = rows * columns * price_projection
#     print(f'{income:.2f}')
# #Killed it. Judge approved

# total_place = rows * columns
# price_ticket = 0 - he does that to avoid writing in the 'if construction'
# Avoid copy-pasting "" or -- from word
# he writes the if counstruction basics from the get go

# --------------------------------------------------------------------------------------
# type_of_the_movie = input()
# rows = int(input())
# columns = int(input())
# total_place = rows * columns
# price_per_ticket = 0
#
# if type_of_the_movie =="Premiere":
#     pass
# elif type_of_the_movie =='Normal':
#     pass
# else: #elif type_of_the_movie =="Discount"
#

# not a good practice to write variables in the if-else construction. Define them outside of the if constructions to find
# mistakes easier and why. Otherwise, it's a mess
#ctrl + alt + l - makes all the = and spaces correct in Python

type_of_the_movie = input()
rows = int(input())
columns = int(input())
total_places = rows * columns
price_per_ticket = 0

if type_of_the_movie == "Premiere":
    price_per_ticket = 12
elif type_of_the_movie == 'Normal':
    price_per_ticket = 7.5
else:  # elif type_of_the_movie =="Discount"
    price_per_ticket = 5

total_income = total_places * price_per_ticket
print(f'{total_income:.2f}')

# CHECK IF YOU CAN REPLACE ELIF WITH IF AND THE CONSTRUCTION STILL WORKS
# sum = count * flower_price   !!!! Don't put those outhere as it performs calculation and fucks up the calculations
# leftover = budget - sum      !!!! Don't put those outhere as it performs calculation and fucks up the calculations
# if count >= 80 and budget >= sum_discount:
#     print(f'Hey, you have a great garden with {count} {flower} and {leftover_discount:.2f} leva left.')
# if count >= 80 and budget < sum_discount:
#     leftover3 = abs(leftover_discount)
#     print(f'Not enough money, you need {leftover3:.2f} leva more.')
