import math

tournament_count = int(input())
initial_points = int(input())

points = 0
count = 0 #This needs to be introduced here, otherwise, it doesn't work. F.e. if you write it first under if stage_tournament =='W'

for i in range(tournament_count):
    stage_tournament = input()
    total = 0
    average = 0
    if stage_tournament == 'W':
        count += 1
        points += 2000
    if stage_tournament == 'F':
        points += 1200
    if stage_tournament == 'SF':
        points += 720

total = initial_points + points
average = math.floor(points / tournament_count)
percent = count/tournament_count*100

print(f'Final points: {total}')
print(f'Average points: {average}')
print(f'{percent:.2f}%')

#Nailed it.100 out of 100