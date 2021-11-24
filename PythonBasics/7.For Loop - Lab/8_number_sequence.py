import sys
numbers = int(input())

smallest = sys.maxsize
biggest = -sys.maxsize

for current_number in range(numbers):
    current_number = int(input())

    if current_number > biggest:
        biggest = current_number
    if current_number < smallest:
        smallest = current_number

print(f'Max number: {biggest}')
print(f'Min number: {smallest}')

#the key to make this work is:
#smallest and biggest are put before the for cycle,
#current number = int(input(), is under the for cycle