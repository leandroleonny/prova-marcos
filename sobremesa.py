from item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def preparar(self) -> str:
        return f"Preparando sobremesa: {self.nome}"