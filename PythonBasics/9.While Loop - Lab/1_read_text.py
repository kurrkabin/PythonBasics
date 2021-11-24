# text = ''
#
# while text != 'Stop':
#     text = input()
#     if text == 'Stop':
#         break
#     print(text)

#Judge approved. By writing text = '', you say text = string, but do NOT input anything. So first value is the input after the
#while loop. This is how you avoid it not reading the first problem
#Judge approved

#Why do we avoid the issue doing it this way?

while True:
    command = input()

    if command =='Stop':
        break

    print(command)