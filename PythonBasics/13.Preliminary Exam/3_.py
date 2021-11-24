number_of_people = int(input())
season = input()
total_price = 0
if number_of_people <= 5:
    if season == "spring":
        price = 50
    elif season == "summer":
        price = 48.5 * 0.85
    elif season == "autumn":
        price = 60
    elif season == "winter":
        price = 86 * 1.08
    total_price = number_of_people * price

if number_of_people > 6:
    if season == "spring":
        price = 48
    elif season == "summer":
        price = 45 * 0.85
    elif season == "autumn":
        price = 49.5
    elif season == "winter":
        price = 85 * 1.08
    total_price = number_of_people * price

print(f'{total_price:.2f} leva.')

#killed it!