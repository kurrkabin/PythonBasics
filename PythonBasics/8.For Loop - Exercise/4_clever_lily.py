age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

total_toys = 0
money_for_each_bday = 0
total_money = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        total_toys += 1
    else:
        money_for_each_bday += 10
        total_money += money_for_each_bday -1 #key is to have this extra total_money, otherwise the money will be 200, instead of 550


price_toys = total_toys * price_per_toy
sum_total = total_money + price_toys
diff = abs(sum_total - washing_machine_price)

if sum_total >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')

