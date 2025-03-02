from src.contato.domain.provider.contato_provider import ContatoProvider

from src.util.cpf_cnpj_util import CpfCnpjUtil
from src.util.errors import NotFoundError

class ContatoGetByDocUseCase:
    
    def __init__(self, doc: str):
        self.doc = doc
        self.provider = ContatoProvider()

    def execute(self):

        docValidator = CpfCnpjUtil(self.doc)

        self.doc = docValidator.unformat()

        if not docValidator.validate(self.doc):
            raise ValueError(f"Documento inválido ",docValidator.format(self.doc))

        contato = self.provider.get_contato_by_doc(self.doc)
        if not contato:
            raise NotFoundError("Contato não encontrado")
        return contato