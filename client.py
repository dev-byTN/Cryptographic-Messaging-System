import socket
import threading
import sys
from kyber_py.ml_kem import ML_KEM_512

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break

            sys.stdout.write('\r' + ' ' * 80 + '\r')
            print(f"[Message] {msg}\n")
        except:
            break

def send_messages( sock):
    while True:
        msg = input("\nEnter a message: ")

        sock.send(msg.encode())

if __name__ =="__main__":

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("127.0.0.1", 5000))

	print("Successful connexion\n")
     
    
    #public_keyA, secret_keyA = ML_KEM_512.keygen()  # 1- Key Generation
    
   # sock.sendall(public_keyA)  #2- Send Public Key to server
    
    #public_keyB = sock.recv(2048)  #3- Encapculation acknowledgment
    
   # keyA, ctA = ML_KEM_512.encapsulate(public_keyB)  #4- Encapsulation
    
    #sock.sendall(ctA)  #5- Send cipher text to server

    #ctB = sock.recv(2048)  #6- Receive cipher text from server

    #final_key = ML_KEM_512.decapsulate(ctB, secret_keyA)  #7- Decapsulation
    
    #print("Shared secret established.")'''

	thread_recv = threading.Thread(target=receive_messages, args=(sock,))
	thread_recv.daemon = True
	thread_recv.start()

	send_messages(sock)

