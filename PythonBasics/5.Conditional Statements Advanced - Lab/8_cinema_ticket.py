day_of_week = input()
price = 0

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Friday':
    price = 12
    print(price)
elif day_of_week == 'Wednesday' or day_of_week == 'Thursday':
    price = 14
    print(price)
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    price = 16
    print(price)

# Beautiful! Here again - you had to put day_of_week each time you wanted to use "or"
