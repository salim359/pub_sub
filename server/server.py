import socket
import sys

def server(port):
    s=socket.socket()
    print('Socket created')
    s.bind(('localhost',port))
    s.listen(3)
    print('waiting for connections')
    
    while True:
        c,addr=s.accept()
        msg=c.recv(1024).decode()
        
        if msg.lower() == 'terminate':
            print('Connected with and terminated',addr)
            c.close()
        else:
            c.send(bytes('Hi client!','utf-8'))
            print('Connected with ',addr)
            print('msg from client:\n',msg)
            c.close()
        
if __name__ == "__main__":
    port=int(sys.argv[1])
    server(port)