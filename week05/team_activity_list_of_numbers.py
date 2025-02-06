"""
Author : Santiago Bergerat 
Team Activity: Lists of Numbers
"""
numbers = []

total_amount= 0
promedio = 0

numero_cercano = 99999999999

while True: 
   number = int(input("Key a number: "))
   if number != 0:
         numbers.append(number)
         total_amount += number
   else:
       break
   
for num  in numbers:
    if num < numero_cercano and num > 0:
        numero_cercano = num
           
   
promedio = total_amount / len(numbers)
print(f"El promedio es: {promedio:.2f}")  

 
max_number = max(numbers)
print ("El numero maximo es: ",max_number)

print("El numero positivo mas cercano a cero es :" ,numero_cercano)

sorted_list= sorted(numbers)

print(f"Lista ordenada  ", end= " ")
for num  in sorted_list:
    print(num, end=" ")
    
