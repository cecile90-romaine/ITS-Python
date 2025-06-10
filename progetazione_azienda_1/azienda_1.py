from re import *
from datetime import datetime

class Importo(float):
    def __new__(cls, v:int|float|str)->self:
        if v < 0:
            raise ValueError("Value v == {v} must be >= 0 ")
        return float.__new__(cls, v)
    
class Dipartimento:
 
nome: str # noto alla nascita
telefono: Telefono # noto alla nascita

def __init__(self)->str:
    
        
        

class _afferenza:
    _impiegato: Impiegato # ovviamento noto alla nascita
    _dipartimento: Dipartimento # ovviamento noto alla nascita e immutabile
    _data_afferenza: data # immutabile, noto alla nasita

def impiegati (self) -> Impiegato:
    return


    
    
class Telefono(str):
    def __new__(cls, v:str)->self:
        if not re.fullmatch(r'\+?[0-9]+', v):
            raise ValueError(f"Vlue v == {v} does  not satisfy the standard")
        
        return str.__new__(cls, v)
    

class Impiegato:
    _nome:str # noto alla nascita
    _cognome:str # noto alla nascita
    _nascita:data#immutabile, noto alla nascita
    _stipendio:Importo # noto alla nascita
    _dipartimento_afferenza:Dipartimento | None # da attribuito di assoc. 'afferenza' [o..1] possibilmente non noto alla nascita
    _data_afferenza:date | None # da attribuito di assoc.'afferenza' immutabile
def __init__(self, nome:str, cognome:str, nascita:data, stipendio: Importo )-> None:
    self.set_nome(nome)
    self.set_cognome(cognome)
    self.nascita = nascita
    self.set_stipendio(stipendio)
    self.set_dipartimento(dipartimento_aff, data_afferenza)

    # o si prendono in input il Dipartimento che la data di afferenza oppure nessuno dei  due
    if  self.dipartimento() and self.dipartimento() is dipartimento_aff

    def nome(self)->str:
        return
        
    def cognome(self)->str:
        return
    def nascita(self)->date: 
        return self._nascita

    def stipendio(self)->Importo:
        return self._stipendio
    

    def set_nome(self, v:str)-> None:
        self._nome = v
    def set_cognome(self, v:str)->None:
        self._cognome = v

    # def set_nascita(self, v:datetime.date)-> None:

    def set_stipendio(self, v:Importo)-> None:
        self._stipendio = v

def __init__(self, nome:str, cognome: str, nascita:datetime:date, stipendio:Importo)->None:
self.set_nome(nome)
self.set_cognome(cognome)
self.set_nascita(nascita)
self.set_stipendio(stipendio)
        
    
