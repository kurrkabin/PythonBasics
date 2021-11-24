number = int(input())

sum=0

while True:
    numbers = int(input())
    sum += numbers
    if sum >= number:
        break
print(sum)

#Judge approved, but it wants you to type in break if sum>=number and print(sum) to be outside the while loop
#Why does it need to be outside