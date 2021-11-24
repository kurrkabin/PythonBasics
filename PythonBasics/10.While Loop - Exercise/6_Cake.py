width = int(input())
length = int(input())
cake = int(width * length)

sum_eaten_pieces = 0

while sum_eaten_pieces < cake:
    eaten_pieces = input()
    if eaten_pieces =='STOP':
        difference = cake - sum_eaten_pieces
        print(f'{difference} pieces are left.')
        break
    sum_eaten_pieces += int(eaten_pieces)
    if sum_eaten_pieces >= cake:
        difference = abs(sum_eaten_pieces - cake)
        print(f'No more cake left! You need {difference} pieces more.')



