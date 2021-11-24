floors = int(input())
flats_per_floor = int(input())

flat_number = 0
flat_name = ''

for x in range(floors, 0, -1):
    for j in range(flats_per_floor):
        flat_number = x * 10 + j
        if x == floors:
            flat_name = f'L{flat_number} '
            print(flat_name, end='')
        elif x % 2 != 0:
            flat_name = f'A{flat_number} '
            print(flat_name, end='')
        elif x % 2 == 0:
            flat_name = f'O{flat_number} '
            print(flat_name, end='')
    print()


