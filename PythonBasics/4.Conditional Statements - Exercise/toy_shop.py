vaccation_price = float(input())
puzzle = int(input())
puppet_talking = int(input())
staffed_bear = int(input())
minion = int(input())
track = int(input())

price_puzzle = puzzle * 2.60
price_puppet_talking = puppet_talking * 3
price_staffed_bear = staffed_bear * 4.1
price_minion = minion * 8.20
price_track = track * 2

count = puzzle + puppet_talking + staffed_bear + minion + track
expenses = price_track + price_minion + price_staffed_bear + price_puppet_talking + price_puzzle
rental = 0.1 * expenses

if count >= 50:
    expenses = expenses * 0.75
    rental = 0.1 * expenses  # if you don't add this here, it's not included in the code
else:
    expenses = expenses * 1  # if you add this here, it works as well
    rental = 0.1 * expenses

winnings = expenses - rental  # if you don't add this after the if count>50, it does not get included
sum = winnings - vaccation_price  # if you don't add this after the if count>50, it does not get included

if sum < 0:
    sum = abs(sum)
    print(f"Not enough money! {sum:.2f} lv needed.")
else:
    print(f"Yes! {sum:.2f} lv left.")

# Yes! Finally, I solved it. Judge approved
