
import random 




answer = "yes"



while answer == "yes":
    
    magic_number = random.randint(1, 100)
    number_user = int(input("Adivina el numero magico: "))
    counter = 1

    while magic_number != number_user : 
        
        if number_user > magic_number :
            print("Lo siento, el numero magico es mas chiquito.. ")
            
        elif number_user < magic_number :
            print ("Lo siento el numero magico es mas grande...")
        
        number_user = int(input("Ingresa el numero de nuevo : "))
        counter = counter + 1
        
    print (f"Felicidades acertaste, tuviste una cantidad de {counter} intentos \n\n")

    answer = input("¿Deseas continuar jugando: 'Yes/ No' " ).lower().strip()

print ("GRACIAR POR JUGAR ")