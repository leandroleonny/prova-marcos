from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def preparar(self) -> str:
        pass