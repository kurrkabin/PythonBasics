fruit = input()
day = input()
quantity = float(input())
price = 0

if day in 'Monday''Tuesday''Wednesday''Thursday''Friday':
    if fruit == 'banana':
        price = 2.5
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'apple':
        price = 1.2
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'orange':
        price = 0.85
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'kiwi':
        price = 2.7
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'pineapple':
        price = 5.5
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'grapes':
        price = 3.85
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit != 'banana' 'apple' 'orange' 'grapefruit' 'kiwi' 'pineapple' 'grapes':
        print('error')
elif day in 'Saturday''Sunday':
    if fruit == 'banana':
        price = 2.7
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'apple':
        price = 1.25
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'orange':
        price = 0.9
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'grapefruit':
        price = 1.6
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'kiwi':
        price = 3
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'pineapple':
        price = 5.6
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit == 'grapes':
        price = 4.2
        price_total = price * quantity
        print(f'{price_total:.2f}')
    elif fruit != 'banana' 'apple' 'orange' 'grapefruit' 'kiwi' 'pineapple' 'grapes':
        print('error')
elif day != 'Monday''Tuesday''Wednesday''Thursday''Friday''Saturday''Sunday':
    print('error')

# The logic goes like this: If it's Monday-Friday, use the prices written for the veggies. If you type in veggies not in the list - you get an error message:

