total_saved = 0

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())

    while budget >= total_saved:
        saved_sum = float(input())
        total_saved += saved_sum
        if total_saved >= budget:
            print(f'Going to {destination}!')
            total_saved = 0
            break

#killed it. Key is to type break in the second while loop and it will re-start the bigger loop.