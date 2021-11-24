day_of_week = input()

if day_of_week in "Monday Tuesday Wednesday Thursday Friday":
    print("Working day")

elif day_of_week in "Saturday Sunday":
    print("Weekend")
else:
    print("Error")

# Works perfectly with "in", but in order to work with "or" you need to specify it each time with "day_of_the_week"
# see the example below

# day_of_week = input()
#
# if day_of_week =="Monday" or day_of_week =="Tuesday" or day_of_week== "Wednesday" or day_of_week =="Thursday" or day_of_week=="Friday":
#     print("Working day")
#
# elif day_of_week in "Saturday Sunday":
#     print("Weekend")
# else:
#     print("Error")
