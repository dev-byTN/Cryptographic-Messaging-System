import socket
import threading

def handle_client(conn, addr, list):
    
    print(f"{addr} Joined the chat")
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"{addr}: {msg}")
        for i in list:
            try:
            	i.send(msg.encode())
            except:
            	pass
            	
    list.remove(conn)
    conn.close()
    
def show_history_message(conn, addr, list):
    
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        for client in list:
            try:
                client.send(msg.encode())
            except:
                pass

    conn.close()
    listUser.remove(conn)

    
if __name__ == "__main__":

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("127.0.0.1", 5000))
	server.listen()

	print("New chat created\n")

	listUser = []

	while True:
	    conn, addr = server.accept()
	    listUser.append(conn)
	    thread1 = threading.Thread(target=handle_client, args=(conn, addr, listUser))
	    thread1.start()
