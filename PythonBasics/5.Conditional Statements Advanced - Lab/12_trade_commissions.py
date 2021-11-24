town = input()
sells = float(input())
commission = 0

if town == 'Sofia':
    if 0 <= sells <= 500:
        commission = 0.05 * sells
        print(f'{commission:.2f}')
    elif 500 < sells <= 1000:
        commission = 0.07 * sells
        print(f'{commission:.2f}')
    elif 1000 <= sells <= 10000:
        commission = 0.08 * sells
        print(f'{commission:.2f}')
    elif sells > 10000:
        commission = 0.12 * sells
        print(f'{commission:.2f}')
    else:
        print('error')
elif town == "Varna":
    if 0 <= sells <= 500:
        commission = 0.045 * sells
        print(f'{commission:.2f}')
    elif 500 < sells <= 1000:
        commission = 0.075 * sells
        print(f'{commission:.2f}')
    elif 1000 <= sells <= 10000:
        commission = 0.1 * sells
        print(f'{commission:.2f}')
    elif sells > 10000:
        commission = 0.13 * sells
        print(f'{commission:.2f}')
    else:
        print('error')
elif town == "Plovdiv":
    if 0 <= sells <= 500:
        commission = 0.055 * sells
        print(f'{commission:.2f}')
    elif 500 < sells <= 1000:
        commission = 0.08 * sells
        print(f'{commission:.2f}')
    elif 1000 <= sells <= 10000:
        commission = 0.12 * sells
        print(f'{commission:.2f}')
    elif sells > 10000:
        commission = 0.145 * sells
        print(f'{commission:.2f}')
    else:
        print('error')
else:
    print('error')

# Killed it! Mission completed!
