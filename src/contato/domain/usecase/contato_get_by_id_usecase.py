from src.contato.domain.provider.contato_provider import ContatoProvider
from src.util.errors import NotFoundError

class ContatoGetByIdUseCase:
    
    def __init__(self, id):
        self.id = id
        self.provider = ContatoProvider()

    def execute(self):
        contato = self.provider.get_contato_by_id(self.id)
        if not contato:
            raise NotFoundError("Contato não encontrado")
        return contato