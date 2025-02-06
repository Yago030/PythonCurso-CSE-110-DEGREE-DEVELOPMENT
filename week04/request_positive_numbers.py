""" 
Author: Santiago Bergerat
*************
Program: Request positive numbers with loop while
"""


number = 0;

while number <= 0 :
    number = int(input("Please type a positive number: " ))
    if number <= 0 :
        print("Sorry, that is a negative number. Please try again.")
    
print("The number is: " ,number)

