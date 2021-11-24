n1 = int(input())
n2 = int(input())
n3 = input()


if n3 == '+':
    result = n1 + n2
elif n3 == '-':
    result  = n1 - n2
elif n3 == '*':
    result  = n1 * n2
elif n3 == '/':
    if n2 ==0:
        print(f'Cannot divide {n1} by zero')
    else:
        result  = n1 / n2
elif n3 == '%':
    if n2 ==0:
        print(f'Cannot divide {n1} by zero')
    else:
        result  = n1 % n2

if n3 == '+' or n3 == '-' or n3 == '*':
    if result  % 2 == 0:
        number = 'even'
    else:
        number = 'odd'

    print(f'{n1} {n3} {n2} = {result } - {number}')

elif n3 == '/' and n2!=0:
    print(f'{n1} / {n2} = {result :.2f}')
elif n3 == '%' and n2!=0:
    print(f'{n1} % {n2} = {result }')


#Judge approved with 100%. I had to enter n2!=0 twice in line 31 and 33
#Key takeaway - avoid using sum as it's built in function and it screws things up


