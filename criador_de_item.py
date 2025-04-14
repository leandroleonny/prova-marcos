from abc import ABC, abstractmethod
from item_cardapio import ItemCardapio

class CriadorDeItem(ABC):
    @abstractmethod
    def criar_item(self) -> ItemCardapio:
        pass