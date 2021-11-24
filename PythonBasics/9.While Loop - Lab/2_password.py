username = input()
password = input()

while True:
    current_password = input()
    if current_password == password:
        break
print(f'Welcome {username}!')

#judge approved. This works w/o even though password could be numbers
