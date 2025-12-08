import socket
import threading

def handle_client(conn, addr):
    
    print(f"[Nouveau client] {addr}")
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"{addr} dit : {msg}")
        addr.send(msg)
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen()

print("Serveur en écoute...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
