budget = float(input())
season = input()

if budget <= 100:
    destination = 'Bulgaria'
elif budget <= 1000:
    destination = 'Balkans'
elif budget > 1000:
    destination = 'Europe'

if season == 'summer' and destination != 'Europe':
    accomodation = 'Camp'
elif season == 'winter' and destination != 'Europe':
    accomodation = 'Hotel'
elif season in 'summer''winter' and destination == 'Europe':
    accomodation = 'Hotel'



if destination == 'Bulgaria' and season == 'summer':
    expenses = budget * 0.3
elif destination == 'Bulgaria' and season == 'winter':
    expenses = budget * 0.7
elif destination == 'Balkans' and season == 'summer':
    expenses = budget * 0.4
elif destination == 'Balkans' and season == 'winter':
    expenses = budget * 0.8
elif destination == 'Europe':
    expenses = budget * 0.9

print(f"Somewhere in {destination}")
print(f'{accomodation} - {expenses:.2f}')

#Killed it. Passed with 100%
