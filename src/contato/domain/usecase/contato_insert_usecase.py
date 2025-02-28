from src.contato.domain.entity.contato_entity_insert import ContatoEntityInsert
from src.contato.domain.provider.contato_provider import ContatoProvider

class ContatoInsertUseCase:
    
    def __init__(self):
        self.entity = ContatoEntityInsert()
        self.provider = ContatoProvider()

    def execute(self):
        self.entity.validate()
        contato = self.provider.get_contato_by_doc(self.entity.doc)

        if contato:
            raise ValueError(f'Contato já cadastrado| (id: {contato['id']}  nome: {contato['nome']})')

        return self.provider.create_contato(self.entity)
