import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(f"[Message] {msg}\n")
        except:
            break

def send_messages(sock):
    while True:
        msg = input("\nEnter a message: ")
        sock.send(msg.encode())

if __name__ =="__main__":

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("127.0.0.1", 5000))

	print("Successful connexion\n")

	thread_recv = threading.Thread(target=receive_messages, args=(sock,))
	thread_recv.daemon = True
	thread_recv.start()

	send_messages(sock)

