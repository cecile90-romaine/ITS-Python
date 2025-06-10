from typing import Self
import re

class Aeroporto:
    _codice: str # <<immutabile>> noto alla nascità
    _nome: str # noto alla nascità

    def __init__(self, codice:str, nome: str) -> None:
        self._codice = codice
        self._set_nome(nome)
        
    def nome( self) -> str:
        return self.nome
    
    def codice(self) -> str:
        return self._codice
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome
