daily_goal = int(input())
sum_price = 0

while True:
    procedure = input()
    if procedure == 'closed':
        break
    gender = input()
    if procedure == 'haircut':
        if gender == 'mens':
            price = 15
        elif gender == 'ladies':
            price = 20
        elif gender == 'kids':
            price = 10
    elif procedure == 'color':
        if gender == 'touch up':
            price = 20
        elif gender == 'full color':
            price = 30
    sum_price += price

    if sum_price >= daily_goal:
        break

difference = daily_goal - sum_price
abs = abs(difference)

if difference >0:
    print(f'Target not reached! You need {abs}lv. more.')
    print(f'Earned money: {sum_price}lv.')
else:
    print("You have reached your target for the day!")
    print(f'Earned money: {sum_price}lv.')

#killed! Yassss.100/100
