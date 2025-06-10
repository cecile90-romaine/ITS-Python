from __future__ import annotations

from esame import *
from Modulo import Modulo

class STudente:
    _nome: str
    _esami:dict[ Modulo , esame._link] # certamente non noto alla nascita
   

    def __init__(self, nome: str) -> None:
       self. _nome = nome

    