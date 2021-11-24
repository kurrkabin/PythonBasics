people_in_group = int(input())
number_sleepovers = int(input())
number_travel_card = int(input())
number_tickets_museum = int(input())

sleepover = 20
travel_card = 1.6
ticket_museum = 6

money_sleepover = number_sleepovers * sleepover
money_travel = number_travel_card * travel_card
money_musem = ticket_museum * number_tickets_museum
sum_one_person = money_sleepover+money_musem+money_travel
sum_all = sum_one_person * people_in_group
added_expenses = sum_all*0.25
sum_total = sum_all+added_expenses

print(f'{sum_total:.2f}')

#solved. Killed it
