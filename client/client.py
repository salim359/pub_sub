import socket
import sys 

def client(server_ip,port):
    c=socket.socket()
    c.connect((server_ip,port))
  
    while True:
        msg=input('Enter your Message to server or terminate (if you want to close the connection):\n')
        while msg.lower() != 'terminate':
            c.send(bytes(msg,'utf-8'))
            print(c.recv(1024).decode()) 
            
        print("Terminating,client.....")
        c.send(bytes(msg,'utf-8'))
        c.close()
        
if __name__ == "__main__":
    server_ip=sys.argv[1]
    port=int(sys.argv[2])
    
    client(server_ip,port)