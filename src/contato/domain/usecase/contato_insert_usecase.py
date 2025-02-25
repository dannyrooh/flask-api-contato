from src.contato.domain.entity.contato_entity_insert import ContatoEntityInsert
from src.contato.domain.provider.contato_provider import ContatoProvider

class ContatoInsertUseCase:
    
    def __init__(self):
        self.usecase = ContatoEntityInsert()

    def execute(self):
        self.usecase.load_from_request()
        self.usecase.validate()

        return ContatoProvider().create_contato(self.usecase)

