
import socket
import json
from server_procedures import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                         
port = 9999
serversocket.bind((host, port))
print("BIND SUCCESSFULLY")                                  
serversocket.listen(5) 
while True:
    # establish a connection
    conn,addr = serversocket.accept()      
    print("Got a connection from %s" % str(addr))    
    msg = conn.recv(1024)
    msg = msg.decode()
    msg=json.loads(msg)

    if msg['procedure_name'] == "foo":
        res=foo(msg['parameters'][0]['value'],)
        conn.sendall(str(res).encode())
    if msg['procedure_name'] == "bar":
        res=bar(msg['parameters'][0]['value'],msg['parameters'][1]['value'],)
        conn.sendall(str(res).encode())
    if msg['procedure_name'] == "random_rating":
        res=random_rating()
        conn.sendall(str(res).encode())