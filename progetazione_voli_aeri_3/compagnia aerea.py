from intg1900 import IntG1900
from città import Citta


class CompagniaAerea:
    _nome: str # noto alla nascità
    _anno_fondazione: IntG1900 # <<immutabile>>, noto alla nascità
    _comp_direzione_citta : Citta   # noto alla nascita

    def __init(self, nome: str, anno_fondazione: IntG1900, citta_sede: Citta) -> None:
        self.set_nome(nome)
        self,_anno_fondazione = anno_fondazione
        self.set_citta_sede(citta_sede)

    def nome(self) -> str:
        return self._nome
    def anno_fondazione(self) -> IntG1900:
        return self._anno_fondazione
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def citta_sede(self) -> Citta:
        return self._comp_direzione_citta
    
    def comp_direzione_citta(self) ->Citta:
        """ Semplice alias di citta_sede()"""
        return self.citta_sede()