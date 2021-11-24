jury_members = int(input())
presentation_name = input()

average_score_all = 0
average_score_presentation = 0
count = 0

while presentation_name != 'Finish':
    for x in range(jury_members):
        current_mark = float(input())
        average_score_all += current_mark
        average_score_presentation += current_mark
        count += 1
    print(f'{presentation_name} - {average_score_presentation / jury_members:.2f}.')
    average_score_presentation = 0

    presentation_name = input()

print(f"Student's final assessment is {average_score_all / count:.2f}.")

#Killed it, though it took me a while. The debbugger helped a lot








# average_score = 0
# score_counter = 0
# all_scores = 0
#
# people_in_jury = int(input())
# presentation_name = input()
#
# while presentation_name != "Finish":
#     total_score = 0
#     for people in range(1,people_in_jury+1):
#         current_score = float(input())
#         score_counter += 1
#         total_score += current_score
#     average_score = total_score / people_in_jury
#     all_scores += total_score
#     print(f"{presentation_name} - {average_score:.2f}.")
#     presentation_name = input()
# print(f"Student's final assessment is {all_scores / score_counter:.2f}.")
#
