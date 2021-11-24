#Key element: Don't write if difference >=0, instead write'if budget >=price_boat." This is what seperated me from getting
#100% and got 93% instead.
#Key take away here is that you can make 3 if constructions. if seasonn==, if fishermen_count == and if season != Autumn
#and fisherman_count %2 ==0. Once the first if construction passes, it goes to the second which goes to the third.
#So this is a very easy way to break down the construction in an easy to read manner
#Second Key take away is use the print at the end outside of the if constructions


budget = int(input())
season = input()
fishermen_count = int(input())
price_boat = 0

if season =="Spring":
    price_boat =3000
    if fishermen_count <= 6 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.9
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')


    elif 7 <= fishermen_count <= 11 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.85
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')

    elif fishermen_count >= 12 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.75
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')

if season =="Summer":
    price_boat =4200
    if fishermen_count <= 6 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.9
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')


    elif 7 <= fishermen_count <= 11 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.85
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')

    elif fishermen_count >= 12 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.75
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')

if season =="Winter":
    price_boat =2600
    if fishermen_count <= 6 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.9
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')


    elif 7 <= fishermen_count <= 11 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.85
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')

    elif fishermen_count >= 12 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.75
        if fishermen_count % 2==0 and season!="Autumn":
            price_boat = price_boat *0.95
            difference = budget - price_boat
            difference2 = abs(budget -price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')
        elif fishermen_count % 2 !=0:
            difference = budget - price_boat
            difference2 = abs(budget - price_boat)
            if budget >= price_boat:
                print(f"Yes! You have {difference:.2f} leva left.")
            elif budget < price_boat:
                print(f'Not enough money! You need {difference2:.2f} leva.')

if season =="Autumn":
    price_boat =4200
    if fishermen_count <= 6 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.90
        difference = budget - price_boat
        difference2 = abs(budget - price_boat)
        if budget >= price_boat:
            print(f"Yes! You have {difference:.2f} leva left.")
        elif budget < price_boat:
            print(f'Not enough money! You need {difference2:.2f} leva.')


    elif 7<= fishermen_count <= 11 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.85
        difference = budget - price_boat
        difference2 = abs(budget - price_boat)
        if budget >= price_boat:
            print(f"Yes! You have {difference:.2f} leva left.")
        elif budget < price_boat:
            print(f'Not enough money! You need {difference2:.2f} leva.')



    elif fishermen_count >=12 and season in 'Spring''Summer' 'Autumn' "Winter":
        price_boat *= 0.75
        difference = budget - price_boat
        difference2 = abs(budget - price_boat)
        if budget >= price_boat:
            print(f"Yes! You have {difference:.2f} leva left.")
        elif budget <price_boat:
            print(f'Not enough money! You need {difference2:.2f} leva.')


#Yaaas! I fucking did it!!