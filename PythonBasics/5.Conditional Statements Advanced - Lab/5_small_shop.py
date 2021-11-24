# product = input()
# city = input()
# quantity = float(input())
# sum1 = 0
# sum2 = 0
# sum3 = 0
#
#
# if city == 'Sofia' and product =='coffee':
#     sum1 = 0.50 * quantity
#     print(sum1)
# elif city == 'Sofia' and product =='water':
#     sum1 = 0.80 * quantity
#     print(sum1)
# elif city == 'Sofia' and product =='beer':
#     sum1 = 1.20 * quantity
#     print(sum1)
# elif city == 'Sofia' and product == 'sweets':
#     sum1= 1.45 * quantity
#     print(sum1)
# elif city == 'Sofia' and product =='peanuts':
#     sum1 = 1.60 * quantity
#     print(sum1)
#
# if city == 'Plovdiv' and product =='coffee':
#     sum2 = 0.40 * quantity
#     print(sum2)
# elif city == 'Plovdiv' and product =='water':
#     sum2 = 0.70 * quantity
#     print(sum2)
# elif city == 'Plovdiv' and product =='beer':
#     sum2 = 1.15 * quantity
#     print(sum2)
# elif city == 'Plovdiv' and product == 'sweets':
#     sum2 = 1.30 * quantity
#     print(sum2)
# elif city == 'Plovdiv' and product =='peanuts':
#     sum2 = 1.50 * quantity
#     print(sum2)
#
# if city == 'Varna' and product =='coffee':
#     sum3 = 0.45 * quantity
#     print(sum3)
# elif city == 'Varna' and product =='water':
#     sum3 = 0.70 * quantity
#     print(sum3)
# elif city == 'Varna' and product =='beer':
#     sum3 = 1.10 * quantity
#     print(sum3)
# elif city == 'Varna' and product =='sweets':
#     sum3 = 1.55 * quantity
#     print(sum3)
# elif city == 'Varna' and product =='peanuts':
#     sum3 = 1.35 * quantity
#     print(sum3)
# #This gets 80-86% from the judge

product = input()
city = input()
quantity = float(input())
price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = 0.5
    elif product == 'water':
        price = 0.8
    elif product == 'beer':
        price = 1.2
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.6
    sum = price * quantity
    print(sum)

if city == 'Plovdiv':
    if product == 'coffee':
        price = 0.4
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.3
    elif product == 'peanuts':
        price = 1.5
    sum = price * quantity
    print(sum)

if city == 'Varna':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.1
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55
    sum = price * quantity
    print(sum)

# this passed with 100% Let's try same but w/o making calcultions in print. The way to do it - just introduce the
# variable sum before you print
