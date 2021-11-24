name = input()
grades_total = 0
count_years = 0
failed_years = 0

while count_years <= 12:
    annual_grade = float(input())
    grades_total += annual_grade
    count_years += 1
    if annual_grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f'{name} has been excluded at {count_years - 1} grade ')
            break
    elif annual_grade >= 4 and count_years == 12:
        average = grades_total / 12
        print(f'{name} graduated. Average grade: {average:.2f}')
        break
