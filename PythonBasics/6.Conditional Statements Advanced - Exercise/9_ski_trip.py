days_spent = int(input())
type_of_accomodation = input()
review = input()

# price_apartment = 0
# price_president =0
# price_room = 0
days_spent = days_spent - 1
if type_of_accomodation == 'apartment':
    price = 25
    if days_spent < 10:
        price *= .7
    elif 10 < days_spent < 15:
        price *= .65
    elif days_spent > 15:
        price *= 0.5

    if review == 'positive':
        price *= 1.25
    elif review == 'negative':
        price *= 0.9

if type_of_accomodation == 'president apartment':
    price = 35
    if days_spent < 10:
        price *= .9
    elif 10 < days_spent < 15:
        price *= .85
    elif days_spent > 15:
        price *= 0.8

    if review == 'positive':
        price *= 1.25
    elif review == 'negative':
        price *= 0.9


if type_of_accomodation == 'room for one person':
    price = 18
    if review == 'positive':
        price *= 1.25
    elif review == 'negative':
        price *= 0.9

total = days_spent * price
print(f'{total:.2f}')

#Solved. 100% judge. Key was to not overcomplicate the solution and do it one by one (type_of_accomodation).
#Another note - doesn't matter
#Another note - if you change elif with if - same shit, passes with 100%. The code is below:

# days_spent = int(input())
# type_of_accomodation = input()
# review = input()
#
# # price_apartment = 0
# # price_president =0
# # price_room = 0
# days_spent = days_spent - 1
# if type_of_accomodation == 'apartment':
#     price = 25
#     if days_spent < 10:
#         price *= .7
#     if 10 < days_spent < 15:
#         price *= .65
#     if days_spent > 15:
#         price *= 0.5
#
#     if review == 'positive':
#         price *= 1.25
#     if review == 'negative':
#         price *= 0.9
#
# if type_of_accomodation == 'president apartment':
#     price = 35
#     if days_spent < 10:
#         price *= .9
#     if 10 < days_spent < 15:
#         price *= .85
#     if days_spent > 15:
#         price *= 0.8
#
#     if review == 'positive':
#         price *= 1.25
#     if review == 'negative':
#         price *= 0.9
#
#
# if type_of_accomodation == 'room for one person':
#     price = 18
#     if review == 'positive':
#         price *= 1.25
#     if review == 'negative':
#         price *= 0.9
#
# total = days_spent * price
# print(f'{total:.2f}')