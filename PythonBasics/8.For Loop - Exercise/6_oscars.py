# actor_name = input()
# total_points = float(input())
# number_of_jury = int(input())
#
# for current_grade in range(number_of_jury):
#     current_name = input()
#     current_points = float(input())
#     current_final_points = len(current_name)*current_points / 2
#     total_points = total_points + current_final_points
#     if total_points > 1250.5:
#         break
#
# if total_points >1250.5:
#     print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
# else:
#     diff = 1250.5 - total_points
#     print(f'Sorry, {actor_name} you need {diff:.1f} more!')
#
# #Judge approved

actor_name = input()
points_academy = int(input())
number_of_judges = int(input())


for i in range(number_of_judges):
    name_of_judge = input()
    points_from_judge = float(input())
    points_judge_system = len(name_of_judge) * points_from_judge / 2
    points_academy += points_judge_system
    if points_academy > 1250.5:
        break

if points_academy > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {points_academy:.1f}!')
else:
    diff = 1250.5 - points_academy
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
