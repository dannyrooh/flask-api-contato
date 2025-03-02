from src.contato.domain.provider.contato_provider import ContatoProvider
from src.util.errors import DeleteError

class ContatoDeleteUseCase:
    
    def __init__(self, id):
        self.id = id
        self.provider = ContatoProvider()

    def execute(self):
        isDelete = self.provider.delete_contato(self.id)
        if not isDelete:
            raise DeleteError("Contato não encontrado")
        return isDelete