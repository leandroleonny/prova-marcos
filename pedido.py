from item_cardapio import ItemCardapio

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: ItemCardapio):
        self.itens.append(item)

    def resumir_pedido(self):
        for item in self.itens:
            print(f"Item: {item.nome}")
            print(f"Preço: R${item.preco:.2f}")
            print(item.preparar())
            print("-" * 30)