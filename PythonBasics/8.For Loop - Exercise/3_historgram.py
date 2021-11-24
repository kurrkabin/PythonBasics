num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(num):
    numbers = int(input())

    if numbers < 200:
        p1 += 1
    elif numbers < 400:
        p2 += 1
    elif numbers < 600:
        p3 += 1
    elif numbers < 800:
        p4 += 1
    else:
        p5 += 1

percent1 = p1/num*100
percent2 = p2/num*100
percent3 = p3/num*100
percent4 = p4/num*100
percent5 = p5/num*100

print(f'{percent1:.2f}%')
print(f'{percent2:.2f}%')
print(f'{percent3:.2f}%')
print(f'{percent4:.2f}%')
print(f'{percent5:.2f}%')


