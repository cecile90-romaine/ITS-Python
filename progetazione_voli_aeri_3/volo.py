from volo import IntGZ
from datetime import timedelta


class Volo:
    _codice: str #  <<immutabile>>, noto alla nascita
    _durata_minuti: IntGZ # noto alla nascità


    def __init__(self, codice:str, durata_minuti: IntGZ) -> None:
        self._codice = codice
        self.set_durata_minuti(durata_minuti)

    def codice(self) -> str:
        return self.codice
    def _durata_minuti(self) -> IntGZ:
        return self._durata_minuti
    
    def durata(self)-> timedelta:
        return timedelta(minutes=self.durata_minuti())
    
    def set_durata_minuti(self, durata: IntGZ) -> None:
        self._durata_minuti = durata