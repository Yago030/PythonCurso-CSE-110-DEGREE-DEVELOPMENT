"""
Author: Santiago Bergerat 
Purpose: Task  Badge Generator 01 First week.
"""
print(" ______________________________________________________________________");
print("|                                                                      |");
print("|                     Welcome to badge generator !!!!                  |");
print("|______________________________________________________________________|\n\n");

first_name= input("Please type your First Name: " ).strip().lower();
last_name = input("Please type your Last Name: " ).strip().upper();
email_adress= input("Please type your Email : " ).strip().lower();
phone_number = input("Please type Phone number: ").strip();
job_title= input("Please type your Job Title: ").strip().title();
id_number= input("Please type your ID Number: ").strip();
hair_color = input("Enter  the  color of  your Hair: ");
eyes_color = input("Enter  the  color of  your Eyes: ");
month = input("Enter month start activity: ");
training = input("Are you in training? (Yes/No): ").strip().lower();
training_bool = training == "Yes"

print("\n The ID Card is:  \n ");
print('-'* 50);
print(f"{last_name} ,  {first_name}");
print(f"{job_title}");
print(f"{id_number} \n");

print(f"{email_adress}");
print(f"{phone_number} \n");



print(f"{'Hair:'} {hair_color:<15} {'Eyes:'} {eyes_color} ");
print(f"{'Month'} {month:<15} {'Training:'} {training_bool} ");
print('-'* 50);