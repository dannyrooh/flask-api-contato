from src.contato.domain.provider.contato_provider import ContatoProvider

class ContatoGetAllUseCase:
    
    def __init__(self):
        self.provider = ContatoProvider()

    def execute(self):
        return self.provider.get_all_contato()
