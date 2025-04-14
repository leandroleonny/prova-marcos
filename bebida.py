from item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def preparar(self) -> str:
        return f"Preparando bebida: {self.nome}"