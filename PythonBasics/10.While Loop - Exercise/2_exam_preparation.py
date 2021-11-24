maximum_failure_amount = int(input())
task_name = input()

failed_times = 0
failed = False
number_of_grades = 0
average_score = 0
last_name = ''

while task_name != 'Enough':
    grade = int(input())
    number_of_grades += 1
    if grade <= 4:
        failed_times += 1
        if failed_times == maximum_failure_amount:
            failed = True
            break
    average_score += grade
    task_name = input()
    if task_name == 'Enough':
        break
    last_name = task_name

average_grade = average_score / number_of_grades

if failed:
    print(f'You need a break, {failed_times} poor grades.')
else:
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {number_of_grades}')
    print(f'Last problem: {last_name}')

