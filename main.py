from criador_de_prato_principal import CriadorDePratoPrincipal
from criador_de_sobremesa import CriadorDeSobremesa
from criador_de_bebida import CriadorDeBebida
from pedido import Pedido

pedido = Pedido()
pedido.adicionar_item(CriadorDePratoPrincipal().criar_item())
pedido.adicionar_item(CriadorDeSobremesa().criar_item())
pedido.adicionar_item(CriadorDeBebida().criar_item())

pedido.resumir_pedido()