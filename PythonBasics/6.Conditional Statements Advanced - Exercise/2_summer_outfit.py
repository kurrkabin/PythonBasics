# celcius = int(input())
# time_of_the_day = input()
#
# if time_of_the_day == "Morning":
#     if 10<= celcius <=18:
#         print(f"It's {celcius} degrees, get your Sweatshirt and Sneakers.")
#     elif 18 < celcius <= 24:
#         print(f"It's {celcius} degrees, get your Shirt and Moccasins.")
#     elif celcius > 25:
#         print(f"It's {celcius} degrees, get your T-Shirt and Sandals.")
# elif time_of_the_day == "Afternoon":
#     if 10 <= celcius <= 18:
#         print(f"It's {celcius} degrees, get your Shirt and Moccasins.")
#     elif 18 < celcius <= 24:
#         print(f"It's {celcius} degrees, get your T-Shirt and Sandals.")
#     elif celcius > 25:
#         print(f"It's {celcius} degrees, get your Swim Suit and Barefoot.")
# elif time_of_the_day == "Evening":
#     if 10 <= celcius <= 18:
#         print(f"It's {celcius} degrees, get your Shirt and Moccasins.")
#     elif 18 < celcius <= 24:
#         print(f"It's {celcius} degrees, get your Shirt and Moccasins.")
#     elif celcius > 25:
#         print(f"It's {celcius} degrees, get your Shirt and Moccasins.")

#Doesn't like this - gets 80% in Judge, probably because I don't have Shirt, Mocassins etc as variables

celcius = int(input())
time_of_the_day = input()
outfit = ''
shoes = ''

if time_of_the_day == "Morning":
    if 10<= celcius <=18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
    elif 18 < celcius <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
    elif celcius >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
elif time_of_the_day == "Afternoon":
    if 10 <= celcius <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
    elif 18 < celcius <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
    elif celcius >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print(f"It's {celcius} degrees, get your Swim Suit and Barefoot.")
elif time_of_the_day == "Evening":
    if 10 <= celcius <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
    elif 18 < celcius <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
    elif celcius >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celcius} degrees, get your {outfit} and {shoes}.")
#Dooone! reason I was getting 80% was because it was celcius >=25 and not just >25.
