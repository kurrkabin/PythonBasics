number_pcs = int(input())
counter_sales = 0
rating_counter = 0
for x in range(number_pcs):
    magic_number = int(input())

    rating = magic_number % 10
    possible_sales = (magic_number - rating) / 10
    if rating == 2:
        possible_sales *= 0
    elif rating == 3:
        possible_sales *= 0.5
    elif rating == 4:
        possible_sales *= 0.7
    elif rating == 5:
        possible_sales *= 0.85
    elif rating == 6:
        possible_sales *= 1
    counter_sales += possible_sales
    rating_counter += rating / number_pcs

print(f'{counter_sales:.2f}')
print(f'{rating_counter:.2f}')

#Smoked it!!!
