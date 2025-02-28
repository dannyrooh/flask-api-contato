from src.contato.domain.provider.contato_provider import ContatoProvider

class ContatoGetByDocUseCase:
    
    def __init__(self, doc: str):
        self.doc = doc
        self.provider = ContatoProvider()

    def execute(self):
        contato = self.provider.get_contato_by_doc(self.doc)
        if not contato:
            raise ValueError("Contato não encontrado")
        return contato