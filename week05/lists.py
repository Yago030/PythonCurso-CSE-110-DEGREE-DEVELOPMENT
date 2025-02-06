clients = []

clients.append("jhon")
clients.append("Mary")


new_client = input("Key new client: ")

clients.append(new_client)

for client in clients:
    print(client)