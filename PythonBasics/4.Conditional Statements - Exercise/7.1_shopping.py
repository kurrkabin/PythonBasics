budget = float(input())
videocards = int(input())  # number of videocards
processors = int(input())  # number of processors
ram = int(input())  # number of ram

price_videocard = 250 * videocards
price_processor = 0.35 * price_videocard * processors
price_ram = ram * 0.1 * price_videocard
total_sum = price_videocard + price_processor + price_ram

if videocards > processors:
    total_sum *= 0.85  # 15% discount

# total_sum = price_videocard + price_processor + price_ram #if I place this here, it changes the calcs and completely removes 15% discount!

difference = abs(total_sum - budget)

if total_sum < budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")

# works like magic this way. It's stupid, but it's judge approved.
