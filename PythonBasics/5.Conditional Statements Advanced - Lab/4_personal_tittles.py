age = float(input())
sex = input()

if age >= 16 and sex == "m":
    print("Mr.")
elif age < 16 and sex == "m":
    print('Master')
elif age >= 16 and sex == "f":
    print("Ms.")
elif age < 16 and sex == "f":
    print("Miss")

# works like this, we don't have to end it with else
# Judge approved. The teacher solved it like this:

# age = float(input())
# sex = input()
#
# if sex =="m":
#    if age <16:
#        print("Master")
#    else:
#        print("Mr.")
# if sex =="f":
#    if age <16:
#        print("Miss")
#    else:
#        print("Ms.")
