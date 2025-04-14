from criador_de_item import CriadorDeItem
from sobremesa import Sobremesa

class CriadorDeSobremesa(CriadorDeItem):
    def criar_item(self) -> Sobremesa:
        return Sobremesa("Pudim", 10.0)