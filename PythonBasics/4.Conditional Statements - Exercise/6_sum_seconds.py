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

winnings = expenses - rental
sum = winnings - vaccation_price

if sum < 0:
    sum = abs(sum)

if sum > 0:
    print(f"Yes! {sum:.2f} lv left.")
else:
    print(f"Not enough money!{sum:.2f} lv needed.")
