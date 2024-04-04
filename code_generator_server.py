import json

file_gen = '''
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
'''

file = open("contract.json")
data = json.load(file)
# Access the data as a dictionary
remote_procedures = data["remote_procedures"]
with open("rpc_server.py","w") as file:
    # for procedure in remote_procedures:
    # file.write(file_gen) 
       
     
    # for procedure in remote_procedures:
    #     file.write("\n")
    #     file.write(str(procedure))
    for i in remote_procedures:
        file_gen+='''
    if msg['procedure_name'] == "{}":
        res={}('''.format(i['procedure_name'],i["procedure_name"])
        for j in range(0,len(i['parameters'])):
            file_gen+="msg['parameters'][{}]['value'],".format(j)
        file_gen+=')\n        conn.sendall(str(res).encode())'
    file.write(file_gen)