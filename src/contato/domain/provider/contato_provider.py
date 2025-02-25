import os
import uuid
import secrets
from src.contato.domain.entity.contato_entity_insert import ContatoEntityInsert
from src.contato.domain.entity.contato_entity_update import ContatoEntityUpdate
from src.contato.infra.contato_repository import ContatoRepository
from src.contato.infra.contato_model import Contato
from src.util.cpf_cnpj_util import CpfCnpjUtil

class ContatoProvider:

    def create_contato(self, entity: ContatoEntityInsert) -> Contato:

        contato = Contato()
        contato.con_nome = entity.nome
        contato.con_ident = entity.ident
        contato.con_codigo = entity.codigo
        contato.con_doc = entity.doc

        if len(entity.doc) == 11:
            contato.con_tipo = 1
        elif len(entity.doc) == 14:
            contato.con_tipo = 2
        else:
            contato.con_tipo = 0

        contato.con_hash = str(uuid.uuid4())
        contato.con_private_token = secrets.randbelow(10000000)
        contato.con_root = os.getenv('ROOT_ID')

        return ContatoRepository().create(contato)
    
    def update_contato(self, entity: ContatoEntityUpdate) -> Contato:
        
        contato_old = self.get_contato_by_id(entity.id)

        if not contato_old:
            raise Exception('Contato não encontrado ou excluído')

        updated_data = {
            "con_nome": entity.nome,
            "con_ident": entity.ident,
            "con_codigo": entity.codigo
        }

        # Atualiza o documento e define o tipo
        if contato_old["doc"] != entity.doc:
            updated_data["con_doc"] = entity.doc

            if len(entity.doc) == 11:
                updated_data["con_tipo"] = 1  # Pessoa física
            elif len(entity.doc) == 14:
                updated_data["con_tipo"] = 2  # Pessoa jurídica
            else:
                updated_data["con_tipo"] = 0  # Tipo indefinido
        else:
            updated_data["con_tipo"] = contato_old["tipo"]
            updated_data["con_doc"] = contato_old["doc"]

        # Mantém os valores antigos
        updated_data["con_hash"] = contato_old["hash"]
        # updated_data["con_private_token"] = contato_old["private_token"]
        updated_data["con_root"] = contato_old["root"]

        return ContatoRepository().update(entity.id, updated_data)


    def get_contato_by_id(self, contato_id: int) -> Contato:
        return ContatoRepository().get_by_id(contato_id)

    def get_contato_by_doc(self, doc: str) -> Contato:
        doc = CpfCnpjUtil(doc).unformat()
        if doc:
            return ContatoRepository().get_by_doc(doc)
        return None

    def get_all_contato(self) -> list:
        return ContatoRepository().get_all()
