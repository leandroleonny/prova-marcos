from criador_de_item import CriadorDeItem
from bebida import Bebida

class CriadorDeBebida(CriadorDeItem):
    def criar_item(self) -> Bebida:
        return Bebida("Suco de Laranja", 7.0)