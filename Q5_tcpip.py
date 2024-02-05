print("""
create file - txt.docx 
enter in file - hello world

---   sender ::  in first notebook --- 
import socket

def main():
    server_port =4000
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sersock:
        sersock.bind(("0.0.0.0",server_port))
        sersock.listen(1)
        print("server ready for connection")
        
        sock,addr = sersock.accept()
        print(f"CONNECTION ESTABLISHED WITH {addr}")
        
        istream = sock.recv(1024).decode()
        fname =istream.strip()
        
        with open(fname,'r') as fileRead:
            for line in fileRead:
                sock.sendall(line.encode())
        
        sock.close()
        sersock.close()
        
if __name__ =="__main__":
    main()
    
output : 
server ready for connection
CONNECTION ESTABLISHED WITH ('127.0.0.1', 50474)



---- receiver ::  in other notebook----

import socket

def main():
    host="127.0.0.1"
    port= 4000
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        
        fname=input("ENTER THE FILE NAME:")
        
        sock.sendall(fname.encode())
        
        data=sock.recv(1024)
        while data:
            print(data.decode(),end ='')
            data =sock.recv(1024)
if __name__== "__main__":
    main()
    
output -- 
ENTER THE FILE NAME:txt.docx""")