budget = float(input())
people = int(input())
uniform_per_person = float(input())

decor = budget * 0.1
price_uniform = people * uniform_per_person

if people > 150:
    price_uniform *= 0.9  # 10% discount

needed_money = price_uniform + decor
difference = abs(needed_money - budget)

if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")

# passes 100% in judge
