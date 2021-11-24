# CHECK IF YOU CAN REPLACE ELIF WITH IF AND THE CONSTRUCTION STILL WORKS
flower = input()
count = int(input())
budget = int(input())
price_flower = 0

if flower == 'Roses':
    price_flower = 5
elif flower == 'Dahlias':
    price_flower = 3.8
elif flower == 'Tulips':
    price_flower = 2.8
elif flower == 'Narcissus':
    price_flower = 3
elif flower == 'Gladiolus':
    price_flower = 2.5

if flower == 'Roses' and count > 80:
    price_flower *= 0.9
elif flower == 'Dahlias' and count > 90:
    price_flower *= 0.85
elif flower == 'Tulips' and count > 80:
    price_flower *= 0.85
elif flower == 'Narcissus' and count < 120:
    price_flower *= 1.15
elif flower == 'Gladiolus' and count < 80:
    price_flower *= 1.2

sum = count * price_flower
leftover = abs(budget - sum)

if budget >= sum:
    print(f'Hey, you have a great garden with {count} {flower} and {leftover:.2f} leva left.')
if budget < sum:
    print(f'Not enough money, you need {leftover:.2f} leva more.')

#YAAASSS! YASAAASSS! Key is - seperate them into a few different if conditions. This way you save so much time and effort!
#Judge approved!
