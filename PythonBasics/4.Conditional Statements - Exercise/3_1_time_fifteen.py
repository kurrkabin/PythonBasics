hour = int(input())
minutes = int(input())

minutes += 15

if minutes > 59:
    minutes = minutes % 60
    hour = hour + 1
if minutes < 9:
    minutes = (f"0{minutes}")
if hour > 23:
    hour = 0

print(f"{hour}:{minutes}")
