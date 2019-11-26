# ---=== HW2 ===---
# Deadline: 01.03.2019 09:00

#--------------------------------------------------------------

# Question-1 (0.2 pts)
# Ask a number from user and count from that number to zero three by three.
# Print a message about whether the number is divisible by three

# Example output-1:
# Give me a number: 11
# 11
# 8
# 5
# 2
# 11 is NOT divisible by 3

# Example output-2:
# Give me a number: 12
# 12
# 9
# 6
# 3
# 12 is divisible by 3

x = int(input('Give me a number: '))
divisible = False
for i in range(x, -1, -3):
    print(i)
    if i == 0:
        divisible = True

if divisible:
    print(str(x) + ' is divisible by 3')
else:
    print(str(x) + ' is NOT divisible by 3')


#--------------------------------------------------------------

# Question-2 (0.3 pts)
# Ask two numbers from user and find the power of smaller number
# by using greater number as exponent

# Example output:
# Give me 1st number: 5
# Give me 2nd number: 3
# Result = 3^5 = 243

x = int(input('number1: '))
y = int(input('number2: '))

if x < y:
    print(x**y)

else:
    print(y**x)

#--------------------------------------------------------------

# Question-3 (0.5 pts)
# Ask two string from user.
# If their lengths are equal, create a new word (and print)
#   by taking the letters from strings one by one (see the example below)
# If their lengths are not equal, create a new word (and print)
#   by adding the shorter string to the end of longer string

# Example output-1:
# Give me 1st string: abcde
# Give me 2nd string: xyztw
# Result: axbyczdtew

# Example output-2:
# Give me 1st string: abcde
# Give me 2nd string: xyzt
# Result: abcdexyzt

# (Hint: If you would like to print your results without new line
#        use print("your string", end="")

x = input('Give me 1st string: ')
y = input('Give me 2nd string: ')

s = ''

if len(x) == len(y):
    for i in range(len(x)):
        s += x[i]
        s += y[i]
elif len(x) < len(y):
    s += y
    s += x

else:
    s += x
    s += y


print(s)

#--------------------------------------------------------------

# Question-4 (OPTIONAL 0.5 pts)
# Take a DNA sequence from the user. If the sequence is a valid DNA sequence.
#   If it is not, print a warning message.
#   If it is, check if it is divisible by 3.
#   If it is divisible by 3, print codons on the screen (assume the first base
#   of the sequence is the first base of the first codon). If it is not, print a
#   warning message.
# Your code should work for both upper and lower case letters.
#  (Hint: Google '.upper()' and '.lower()')

# Example output-1:
# Give me a DNA sequence: actagctgacxg
# This is not a valid DNA sequence

# Example output-2:
# Give me a DNA sequence: agctagcatcgac
# DNA sequence is not divisible by 3

# Example output-3:
# Give me a DNA sequence: agctagcatcga
# agc
# tag
# cat
# cga

x = input('give me a DNA sequence: ')
valid_dna = 'acgtACGT'
valid = True
k = 0

for i in x:
    if i not in valid_dna:
        valid = False

if valid:
    if len(x) % 3 == 0:
        for i in range(0, len(x), 3):
            print(x[i:i+3])
    else:
        print( 'DNA Sequence is not divisible by 3')

else:
    print('NOT VALID')

