from src.contato.domain.entity.contato_entity_update import ContatoEntityUpdate
from src.contato.domain.provider.contato_provider import ContatoProvider

class ContatoUpdateUseCase:
    
    def __init__(self):
        self.entity = ContatoEntityUpdate()
        self.provider = ContatoProvider()

    def execute(self):
        self.entity.validate()
        contato = self.provider.get_contato_by_doc(self.entity.doc)

        if contato and (contato['id'] != self.entity.id):
            raise ValueError(f'Existe um outro Contato ja cadastrado com o CNPJ/CPF informado! (id: {contato["id"]}  nome: {contato["nome"]})')

        return self.provider.update_contato(self.entity)

