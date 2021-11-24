exam_hour = int(input())
exam_minute = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

exam_time = exam_hour * 60 + exam_minute
exam_arrival = hour_arrival * 60 + minute_arrival

difference = exam_time - exam_arrival
differenceabs = abs(exam_time - exam_arrival)

if exam_arrival > exam_time:
    print('Late')
elif exam_time - exam_arrival <= 30:
    print('On time')
elif exam_time - exam_arrival > 30:
    print('Early')

if 0 < difference < 60:
    print(f'{difference} minutes before the start')
elif difference >=60:
    hour = difference // 60
    minutes = difference % 60
    if minutes <=9:
        print(f'{hour}:0{minutes} hours before the start')
    elif minutes >10:
        print(f'{hour}:{minutes} hours before the start')
elif differenceabs <=59:
    print(f'{differenceabs} minutes after the start')
elif differenceabs >=60:
    hour = differenceabs // 60
    minutes = differenceabs % 60
    if minutes <= 9:
        print(f'{hour}:0{minutes} hours after the start')
    elif minutes > 10:
        print(f'{hour}:{minutes} hours after the start')

#Killed it.Judge approved. The only key takeaways are:
#-convert hour and minutes to minutes in order to see what's what
#-the use of differenceabs was quite quite too.