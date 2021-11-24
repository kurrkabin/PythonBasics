import math
from math import ceil

tv_series_name = (input())
tv_series_length = int(input())
length_of_break = int(input())

time_lunch = 0.125 * length_of_break
time_rest = 0.25 * length_of_break
time_to_watch = length_of_break - time_lunch - time_rest
difference = time_to_watch - tv_series_length
difference2 = abs(difference)
difference3 = math.ceil(difference2)

if difference >= 0:
    print(f"You have enough time to watch {tv_series_name} and left with {difference3} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series_name}, you need {difference3} more minutes.")

