import json

PATH: str = "lezione_15/codice_fisc.json"
mode: str = "r"

with open(PATH, mode = mode) as file:
    codice_fisc:dict = json.load(file)
codice_fisc["A12345C306"] = {"nome":"Alice","cognome":"Conti", "eta":"30"}

with open (PATH, mode = "w") as file:
    json.dump(codice_fisc, file, indent = 4)
   

