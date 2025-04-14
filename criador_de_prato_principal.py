from criador_de_item import CriadorDeItem
from prato_principal import PratoPrincipal

class CriadorDePratoPrincipal(CriadorDeItem):
    def criar_item(self) -> PratoPrincipal:
        return PratoPrincipal("Lasanha", 25.0)