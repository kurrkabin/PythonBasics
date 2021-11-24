starting = int(input())
end = int(input())
magic_number = int(input())

combinations = 0
result = 0

combinations_result = False

for x in range(starting, end + 1):
    for y in range(starting, end + 1):
        result = x + y
        combinations += 1
        if result == magic_number:
            combinations_result = True
            break
    if combinations_result:
        break

if combinations_result:
    print(f"Combination N:{combinations} ({x} + {y} = {magic_number})")
else:
    print(f'{combinations} combinations - neither equals {magic_number} ')

#Key is to insert line 17: if combination results = break. Otherwise, the shit continues and/or prints the combinations.
#Judge approved