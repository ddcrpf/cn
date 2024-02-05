print("""
 
 -- code for part 1 ----
 
import socket
import sys

def main():
    print("ENTER THE FILENAME")
    filename= input().strip()
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sersock:
        sersock.bind(('localhost',4000))
        sersock.listen()
        
        print("SERVER READY FOR CONNECTION")
        
        with sersock.accept() as (sock,addr), sock.makefile('r') as file_read:
            print(f"connection is succesfull and waiting for client request from {addr}")
            file_read.readline()
            
            try:
                with open(filename,'r') as content_read, sock.makefile('w') as pwrite:
                    for line in content_read:
                        pwrite.write(line)
            except FileNotFoundError:
                print(f"Error: File {filename} not found.")

if __name__ == "__main__":
    main()
     
     
-- code for part 2 as per mam---   
        
import socket

def main():
    server_port= 4444
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.bind(('0.0.0.0',server_port))
        print("waiting.....")
        
        data, addr = sock.recvfrom(256)
        message = data.decode()
        
        print(f"{addr[0]}:{addr[1]}-{message}")
        
if __name__== "__main__":
    main()
        
    





--- code for part 2 that works -- 
import socket

def main():
    server_port= 4444
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.bind(('0.0.0.0',server_port))
        sock.listen(1)  # Listen for incoming connections
        print("waiting.....")
        
        conn, addr = sock.accept()  # Accept a connection
        with conn:
            data = conn.recv(256)  # Receive data from the connection
            message = data.decode()
        
            print(f"{addr[0]}:{addr[1]}-{message}")
        
if __name__== "__main__":
    main()""")