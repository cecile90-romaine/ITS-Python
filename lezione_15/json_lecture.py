import json

'''
PATH:str = "lezione_15/config.json"
mode:str = "r"
with open(PATH, mode= mode)as file:
    config:dict = json.load(file)
    print(config)

    nome_applicazione:str = config["appName"]

    host:str = config["server"]["host"]
    port: str = str(config["server"])["port"]
    timeout:int = config["server"]["timeout"]

    connect(ip=host, port=port, timeout=timeout)
    
    print(nome_applicazione)'''

PATH:str = "lezione_15/config.json"
mode:str = "w"
config:dict = {}

with open(PATH, mode="r") as file:
    config = json.load(file)

config["server"]["host"] = "facebook.com"
config["server"]["port"] = 5000
with open(PATH, mode="w") as file:

  with open(PATH, mode=mode) as file:

    config:dict = {"nome": " 2048", " versione": "1.1.42", "OS": "android 16.1.0"}
    
    json.dump(config, file, indent=4)


# 1) crea un file json usando i comandi touch , enano.leggere il file appena creato e stampare un valore
#2) crea un file json da python salvndo un dizionario a vostra scelta.

# 3) crea un file json usando touch e nano, che contiene codice fiscale come chiave e come valore diczionarii che
# contengono nome , cognome ed età della persona ( almeno) e poi modificare il json aggiungendo una personna.