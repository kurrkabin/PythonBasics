open_browsers = int(input())
salary = int(input())

for i in range(open_browsers):
    site_name = input()
    if site_name == 'Facebook':
        salary -= 150
    elif site_name == 'Instagram':
        salary -= 100
    elif site_name == 'Reddit':
        salary -= 50
    elif site_name =="Pornhub" or site_name =='xvideos.com':
        print('Outta Boy!')
    if salary <= 0:
        break

if salary <= 0:
    print(f'You have lost your salary.')
elif salary > 0:
    print(salary)

# Killed it. 100% Judge approved. The important here is to break the cycle if salary gets under or equal to zero
