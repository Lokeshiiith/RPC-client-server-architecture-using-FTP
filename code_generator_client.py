import json

file_str = '''
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
'''

contract=json.load(open("contract.json"))
f=open("rpc_client.py","w+")
func_str='''
def {}({}):
    msg=dict()
    msg["procedure_name"]="{}"
    msg["parameters"]=list()
    msg["return_type"]="{}"'''
for i in contract["remote_procedures"]:
    parameters=""	
    for j in i["parameters"]:
        parameters+=j["parameter_name"]+','
    file_str=file_str+func_str.format(i["procedure_name"],parameters,i["procedure_name"],i["return_type"])
    for j in i["parameters"]:
        file_str+="\n    msg['parameters'].append({{'parameter_name':'{}','data_type':'{}','value':{}}})".format(j["parameter_name"],j["data_type"],j["parameter_name"])
    file_str+='''
    resp_from_server=msg_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return {}(resp_from_server)
    '''.format("str" if i['return_type']=="string" or i['return_type']=="void"  else i['return_type'])
# print(file_str)
f.write(file_str)


