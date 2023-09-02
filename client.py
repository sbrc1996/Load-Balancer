import socket

#Load Balancer Details.
IP = '127.0.0.1'
LOAD_PORT = 19345
FORMAT = "utf-8"

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)    		#Connecting to the Load Balancer.
client.connect((IP,LOAD_PORT)) 

try:
    while True:
        message = input("Enter a message: ")
        client.send(message.encode(FORMAT))
        response = client.recv(1024).decode(FORMAT)
        print(f"Repsonse from server-> {response}") 
        message = input("Do you want to Continue? y or n")
        client.send(message.encode(FORMAT))
        if message.lower() == "y" or message.lower() == "yes":
            continue
        else:   
            break
except Exception as e:
    print(f"Exception occured as {e}")
finally:
    print("Connection terminated by the client.")
    client.close()

