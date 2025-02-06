clients = []
new_client = ""

while new_client != "Quite":
    new_client = input("Name new clien: ").capitalize()
    if new_client != "Quite":
         clients.append(new_client)
    
    
print( "The new clients are: ")
for client in clients:
    print(client)
    