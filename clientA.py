import socket
import dotenv
import os
from kyber_py.ml_kem import ML_KEM_512


"""secret_key, public_key = ML_KEM_512.keygen() # 1 - Key Generation
with open("secret_keyA.txt", "w") as f:
    f.write(public_key) # 2 - Store Public Key"""
    
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

while True:
    
    dotenv.load_dotenv()
    clientB_key = os.getenv("SECRET_KEY_B")
    
    msg = input("Message : ")
    client.send(msg.encode())
    
    response = client.recv(1024).decode()
    print(f"Serveur dit : {response}")
    

