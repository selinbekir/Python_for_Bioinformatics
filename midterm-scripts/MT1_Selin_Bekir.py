
'''
Ask user to input a number.
When user inputs 5 numbers, stop asking and return the sum of that 5 numbers 
Ignore the non-integer inputs
'''


X = int(input('please enter X: '))


valid = False
input_listem = []

while valid == False:
    myinput = input('Program: Please input number')
    if myinput.isnumeric():
        input_listem.append(myinput)

    if len(input_listem) == X:
        valid = True

intlist = []
if valid:
    for i in input_listem:
        i = int(i)
        intlist.append(i)
    print('OK: You summed up to:', sum(intlist))




