number_of_groups = int(input())

sum_of_all_people = 0
people_5 = 0
people_12 = 0
people_25 = 0
people_40 = 0
people_41 = 0

for x in range(number_of_groups):
    people_in_a_group = int(input())
    if people_in_a_group <= 5:
        people_5 += people_in_a_group
        sum_of_all_people += people_in_a_group
    elif people_in_a_group <= 12:
        people_12 += people_in_a_group
        sum_of_all_people += people_in_a_group
    elif people_in_a_group <= 25:
        people_25 += people_in_a_group
        sum_of_all_people += people_in_a_group
    elif people_in_a_group <= 40:
        people_40 += people_in_a_group
        sum_of_all_people += people_in_a_group
    elif people_in_a_group >= 41:
        people_41 += people_in_a_group
        sum_of_all_people += people_in_a_group

total = sum_of_all_people

percent_5 = people_5/total*100
percent_12 = people_12/total*100
percent_25 = people_25/total*100
percent_40 = people_40/total*100
percent_41 = people_41/total*100

print(f'{percent_5:.2f}%')
print(f'{percent_12:.2f}%')
print(f'{percent_25:.2f}%')
print(f'{percent_40:.2f}%')
print(f'{percent_41:.2f}%')

#Killed it, dawwwg!