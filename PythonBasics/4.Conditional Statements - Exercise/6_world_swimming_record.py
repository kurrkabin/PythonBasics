import math
from math import ceil

record_in_seconds = float(input())  # record time in seconds that Ivan needs to break
distance_meters = float(input())  # distance that Ivan needs to swim
meters_swum_per_second_ = float(input())  # time_in_seconds that Ivan swims 1 meter

time_swimming_in_seconds = distance_meters * meters_swum_per_second_
x = distance_meters / 15
x1 = math.floor(x)
extra_time = x1 * 12.5

if distance_meters >= 15:
    time_swimming_in_seconds = extra_time + time_swimming_in_seconds

time_record_vs_time_ivan = abs(time_swimming_in_seconds - record_in_seconds)

if time_swimming_in_seconds >= record_in_seconds:
    print(f"No, he failed! He was {time_record_vs_time_ivan:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {time_swimming_in_seconds:.2f} seconds.")

# perfection! Judge approved
