


with open("web_traffic.csv") as data:
   for line in data:
       print(line)
 
       parts= line.split(",")
        
       page=parts[0].strip()
       time= parts[1].strip()
       referring_page = parts[2].strip()
        
       print(f"Páge '{page}' referred by '{referring_page}' was visited for '{time}' seconds  ")