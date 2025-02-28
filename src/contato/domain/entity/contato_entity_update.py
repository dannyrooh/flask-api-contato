from src.contato.domain.entity.contato_entity import ContatoEntity

class ContatoEntityUpdate(ContatoEntity):

    def validate(self):
        if not self.id:
           raise ValueError("Id do contato deve ser informado!") 
        pass
