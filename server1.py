import socket
import threading

IP = '127.0.0.1'
PORT = 19346
FORMAT = "utf-8"

server_address = (IP,PORT)

print(f"Server 1 is starting...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server 1 listening on", server_address)


def handle_client(client_conn, client_addr):
    print(f"Client from {client_addr} has connected..")
    try:
        while True:
            msg = client_conn.recv(1024).decode(FORMAT)
            print(f"Message from client is {msg}.")
            response = "Message successfully recieved."
            client_conn.send(response.encode(FORMAT))
            msg = client_conn.recv(1024).decode(FORMAT)
            if msg.lower() == "y" or msg.lower() == "yes":
                continue
            else:
                 break 
    except Exception as e:
        print(f"Error {e} has occured.")
    finally:        
        print("Connection terminated by the client.")
        client_conn.close()

while True:
    conn, addr = server_socket.accept()                                 #A client came from the load_balancer and connected to the server..
    thread = threading.Thread(target=handle_client, args= (conn,addr))
    thread.start()


