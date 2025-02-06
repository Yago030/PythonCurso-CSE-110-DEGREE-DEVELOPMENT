"""
Author: Santiago Bergerat 
Purpose: Meal Price Calculator

Calculates the subtotal by adding the total cost of children's and adults' meals
Multiplies the price by the quantity for each type of meal and sums up the results

Additional Features:
- Option to add a tip for the waiter, with input validation.
- Ensures the payment amount is sufficient before proceeding.
"""

#intro
print ('-' *50)
print (f'{" Meal Price Calculator":^50}')
print ('-'*50)

#variables
child_meal = float(input("What is the price of a child's meal?:  $"))
adult_meal = float(input("What is the price of an adult's meal?:  $"))
children_number = int(input('How many children are there?: '))
adults_number = int(input('How many adults are there?: '))

#Calculate subtotal
subtotal = (child_meal * children_number) + (adult_meal * adults_number)
print(f'\nSubtotal: ${subtotal:.2f}\n')
 


"""
  -------------------- Milestone Submission --------------------
The following code completes the required milestone features:
- Ask for meal prices and quantities
- Calculate and display the subtotal

"""


#tax calculation
tax = float(input("What is the sales tax rate?:  $"))
tax_calculation = (subtotal * tax) / 100
total = subtotal + tax_calculation

print(f'Sales Tax: ${tax_calculation:.2f}')
print(f'Total: ${total:.2f} \n')

#tip
print('\nWould you like to add a tip for the waiter?: \n')
tip = input(f"{'Yes':>20} / {'No':<20}: \n ").capitalize()

if(tip == 'Yes'):
    tip_amount = float(input('What is the tip  amount?: $'))
    while(tip_amount <= 0):
        print("Sorry, tip amount must be greater THAN 0. Please try again. !!!")
        tip_amount = float(input('What is the tip amount?: $'))

    total = total + tip_amount


#Payment calculation
payment_amount = float(input('\nWhat is the payment amount?: $'))
while payment_amount < total :
    print ('-' *50)
    print (f'{"¡¡¡  WARNING !!!":^50}')
    print ('-'*50)
    print('\nInsufficient payment amount. Please try again... \n')
    payment_amount = float(input('New payment amount?: $'))
    
change = payment_amount - total
print(f'Change: ${change:.2f}')

