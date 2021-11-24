flower = input()
count = int(input())
budget = int(input())

if flower in 'Roses''Dahlias''Tulips' 'Narcissus''Gladiolus':
    if flower =="Roses":
        if count >=80:
            price_flower = 4.5
            sum = count * price_flower
            leftover = budget - sum
            leftover1 = abs(leftover)
            if budget >= sum:
                print(f'Hey, you have a great garden with {count} {flower} and {leftover:.2f} leva left.')
            if budget < sum:
                print(f'Not enough money, you need {leftover1:.2f} leva more.')

        elif count <80:
            price_flower = 5
            sum = count * price_flower
            leftover = budget - sum
            leftover1 = abs(leftover)
            if budget >= sum:
                print(f'Hey, you have a great garden with {count} {flower} and {leftover:.2f} leva left.')
            if budget < sum:
                print(f'Not enough money, you need {leftover1:.2f} leva more.')

    elif flower =="Dahlias":
        if count >= 90:
            price_flower = 3.23
            sum = count * price_flower
            leftover = budget - sum
            leftover1 = abs(leftover)
            if budget >= sum:
                print(f'Hey, you have a great garden with {count} {flower} and {leftover:.2f} leva left.')
            if budget < sum:
                print(f'Not enough money, you need {leftover1:.2f} leva more.')

        elif count < 80:
            price_flower = 3.8
            sum = count * price_flower
            leftover = budget - sum
            leftover1 = abs(leftover)
            if budget >= sum:
                print(f'Hey, you have a great garden with {count} {flower} and {leftover:.2f} leva left.')
            if budget < sum:
                print(f'Not enough money, you need {leftover1:.2f} leva more.')