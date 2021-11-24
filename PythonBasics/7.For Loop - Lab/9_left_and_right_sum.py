n = int(input())

left_side = 0

for i in range(n):
    current_number = int(input())
    left_side += current_number

right_side = 0

for i in range(n):
    current_number = int(input())
    right_side+= current_number


if left_side == right_side:
    print(f'Yes, sum = {left_side}')

elif left_side != right_side:
     difference = abs(left_side - right_side)
     print(f'No, diff = {difference}')

#My code. Essentially, we have to enter left_side before the cycle. Why - I have no fucking idea
