
"""
Author: Santiago Bergerat 
Purpose: W03 Team work Grade calculator program

"""

percentege = float(input('Type a note : '))

# secont  part  
if (percentege >= 90):
    print('Your calification is A ')
elif (percentege >= 80):
    print('Your calification is B ')
elif (percentege >= 70):
    print('Your calification is C ')
elif (percentege >= 60):
    print('Your calification is D ')
else :
    print('Your calification is F ')

if( percentege >= 70 ): 
    print('Congratulations, you passed the course!')
else:
    print('Keep trying, you almost made it!')
    
    

letter = ""

if (percentege >= 90):
    letter = "A"
elif (percentege >= 80):
    letter = "B"
elif (percentege >= 70):
    letter = "C"
elif (percentege >= 60):
    letter = "D"
else :
    letter = "F"

print (f'Your calification is : {letter}. ')


# Stretch Challenge Step 1-2 -3  
# Purpose: Determine and display letter grades, including +/-.

last_digit = int(percentege) % 10
if last_digit >= 7:
    sign = '+'
elif last_digit < 3:
    sign = '-'
else:
    sign = ''  

if letter == 'A' and sign == '+':
    sign = ''  
if letter == 'F':
    sign = ''
    
    
print(f'Your calification is : {letter}{sign}. ')
