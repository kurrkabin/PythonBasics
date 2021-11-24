width = int(input())
length = int(input())
height = int(input())

room = width * length * height
luggage = 0

while luggage < room:
    command = input()
    if command == "Done":
        difference = room - luggage
        print(f'{difference} Cubic meters left.')
        break
    luggage += int(command)
    if luggage >= room:
        difference = abs(luggage - room)
        print(f'No more free space! You need {difference} Cubic meters more.')
        break

