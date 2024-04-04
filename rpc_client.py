
import socket 
import json


file = open("contract.json")
data = json.load(file)
# Access the data as a dictionary
remote_procedures = data["remote_procedures"]

def msg_to_server(msg):
    port = 9999
    # get local machine name
    host = socket.gethostname() 
    # # create a socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host,port))
    msg = json.dumps(msg)
    clientsocket.send(msg.encode('utf-8'))
    
    # # receive data from the server
    data = clientsocket.recv(1024)
    clientsocket.close()
    return data

def foo(par_1,):
    msg=dict()
    msg["procedure_name"]="foo"
    msg["parameters"]=list()
    msg["return_type"]="str"
    msg['parameters'].append({'parameter_name':'par_1','data_type':'int','value':par_1})
    resp_from_server=msg_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return str(resp_from_server)
    
def bar(par_1,par_2,):
    msg=dict()
    msg["procedure_name"]="bar"
    msg["parameters"]=list()
    msg["return_type"]="str"
    msg['parameters'].append({'parameter_name':'par_1','data_type':'int','value':par_1})
    msg['parameters'].append({'parameter_name':'par_2','data_type':'str','value':par_2})
    resp_from_server=msg_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return str(resp_from_server)
    
def random_rating():
    msg=dict()
    msg["procedure_name"]="random_rating"
    msg["parameters"]=list()
    msg["return_type"]="int"
    resp_from_server=msg_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return int(resp_from_server)
    