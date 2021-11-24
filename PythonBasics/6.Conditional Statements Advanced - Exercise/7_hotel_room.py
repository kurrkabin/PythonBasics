month = input()
sleepovers = int(input())

# studio =0
# apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77


if 7 < sleepovers < 14:
    if month == 'May' or month == 'October':
        studio *= 0.95
elif sleepovers > 14:
    if month == 'May' or month == 'October':
        studio *= 0.7
        apartment*=0.9
    elif month in 'June''September':
        apartment*=0.9
        studio*=0.8
    elif month in "July" "August":
        apartment*=0.9

result = sleepovers * apartment
result2 = sleepovers * studio

print(f'Apartment: {result:.2f} lv.')
print(f'Studio: {result2:.2f} lv.')


# Yaassss! Done it. 100 judge approved.