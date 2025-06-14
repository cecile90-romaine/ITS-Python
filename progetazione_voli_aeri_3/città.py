from città import IntGEZ


class Citta:
    _nome: str
    _abitanti: IntGEZ

    def __init__(self, nome: str, abitanti: IntGEZ) -> None:
        self.set_nome(nome)
        self.set_abitanti(abitanti)
        

    def nome(self) -> str:
        return self._nome
    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def abitanti(self) -> None:
        return self._abitanti
    
    def set_abitanti(self, abitanti: IntGEZ) -> None:
        self._abitanti = abitanti