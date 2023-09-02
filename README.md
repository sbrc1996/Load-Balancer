Implementing a Load Balancer using Python and Socket Programming. 
This project has multiple clients, 2 server and a load balancer.

To start the project first run both the server -> load balancer -> clients(multiple instances) through the terminal

The screenshot of the project:
![Screenshot from 2023-09-02 13-37-15](https://github.com/sbrc1996/Load-Balancer/assets/36306295/ac9c7cae-a067-4a1b-9ece-ab98729d9252)


Future Prospect :

Implement a file handling mechanism.
Where in both the server will have a common file that will store the key- value pairs in it.
If a client want to insert data into it, first find through the file if it exists or not?
If exists -> then apply a record lock on the record and update it.
If not exists -> then enter the data into the file @ the end.

Implement this entire thing using Fcntl and Lseek in python.

