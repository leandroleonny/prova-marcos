from item_cardapio import ItemCardapio

class PratoPrincipal(ItemCardapio):
    def preparar(self) -> str:
        return f"Preparando prato principal: {self.nome}"