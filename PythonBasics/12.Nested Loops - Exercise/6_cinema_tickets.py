movie_name = input()

student_tickets = 0
kids_tickets = 0
standard_tickets = 0
overall_tickets = 0
game_over = False

current_overall_tickets = 0

while movie_name != "Finish":
    available_seats = int(input())
    free_seats = available_seats
    while free_seats >= 0:
        type_ticket = input()
        if type_ticket == 'End':
            print(f'{movie_name} - {current_overall_tickets / available_seats * 100:.2f}% full.')
            current_overall_tickets = 0
            break
        if type_ticket == 'student':
            student_tickets += 1
            current_overall_tickets += 1
        elif type_ticket == 'kid':
            kids_tickets += 1
            current_overall_tickets += 1
        elif type_ticket == 'standard':
            standard_tickets += 1
            current_overall_tickets += 1
        overall_tickets = standard_tickets + kids_tickets + student_tickets
        free_seats-=1
        if free_seats == 0:
            print(f'{movie_name} - {current_overall_tickets / available_seats * 100:.2f}% full.')
            current_overall_tickets = 0
            break
    if game_over:
        print(f'{movie_name} - {current_overall_tickets / available_seats * 100:.2f}% full.')
        break
    movie_name = input()

student_percentage = student_tickets / overall_tickets * 100
standard_percentage = standard_tickets / overall_tickets * 100
kids_percentage = kids_tickets / overall_tickets * 100

print(f'Total tickets: {overall_tickets}')
print(f'{student_percentage:.2f}% student tickets.')
print(f'{standard_percentage:.2f}% standard tickets.')
print(f'{kids_percentage:.2f}% kids tickets.')


