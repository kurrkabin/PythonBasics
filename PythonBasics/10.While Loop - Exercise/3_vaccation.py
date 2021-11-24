money_needed_for_trip = float(input())
saved_money = float(input())

consecutive_days_spending = 0
overall_days = 0

while saved_money < money_needed_for_trip and consecutive_days_spending < 5:
    action = input()
    money = float(input())
    overall_days += 1
    if action == 'save':
        saved_money += money
        consecutive_days_spending = 0
        if saved_money >= money_needed_for_trip:
            print(f'You saved the money for {overall_days} days.')
            break
    elif action == 'spend':
        saved_money -= money
        consecutive_days_spending += 1
        if saved_money < 0:
            saved_money = 0
        if consecutive_days_spending == 5:
            print("You can't save the money.")
            print(overall_days)
            break


#Passed by the judge.