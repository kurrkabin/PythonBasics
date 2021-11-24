import sys
biggest = -sys.maxsize
while True:
    number = input()
    if number == "Stop":
        break
    elif float(number) > biggest:
        biggest = float(number)

print(int(biggest))

#Works, 100%
