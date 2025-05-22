import json

                                                  # prima ho creato dal terminale un file dict.json in cui messo un dizionario
with open("lezione_15/dict.json", "r") as file: # ho creato un file python example.py e ho  importato in avevo salvato un dizionario
    dizionario: dict = json.load(file)
    print(dizionario["libro1"])