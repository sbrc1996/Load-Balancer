import socket
import threading


IP = '127.0.0.1'
LOAD_PORT = 19345
SERVER1_PORT = 19346
SERVER2_PORT = 19347
FORMAT = "utf-8"

server_address = [(IP,SERVER1_PORT),(IP,SERVER2_PORT)]
current_server = 0


def handle_client(client_conn, client_addr):
    print(f"Client from {client_addr} has connected..")
    while True:
        try:
            msg = client_conn.recv(1024).decode(FORMAT)
            print(f" Message from client is {msg}.")
            msg = "Message successfully recieved."
            client_conn.send(msg.encode(FORMAT))
            msg = client_conn.recv(1024).decode(FORMAT)
            if msg.lower() != "y" or msg.lower() != "yes":
                break   
        except Exception as e:
                print(f"Error {e} has occured.")
        finally:
            print("Connection terminated by the client.")
            client_conn.close()



# def start_server(server_addr):
#     server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
#     server.bind((server_addr))
#     server.listen(5)
#     print(f"Server listening @ {server_addr[0]}:{server_addr[1]}")
#     return server


while True:
    client_conn,client_addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_conn,client_addr))
    thread.start()

#Starting the load Balancers..
load_balancer_server = start_server((IP,LOAD_PORT))


#Starting the servers..
for server in server_address:
    start_server(server)
