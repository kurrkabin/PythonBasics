import sys

smallest = sys.maxsize

while True:
    number = input()
    if number == 'Stop':
        break
    elif int(number) < smallest:
        smallest = int(number)
print(smallest)

# Judge approved.
