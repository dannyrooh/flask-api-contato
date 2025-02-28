from src.util import handler_controller as handler

from src.contato.domain.usecase.contato_insert_usecase import ContatoInsertUseCase
from src.contato.domain.usecase.contato_update_usecase import ContatoUpdateUseCase
from src.contato.domain.usecase.contato_get_all_usecase import ContatoGetAllUseCase
from src.contato.domain.usecase.contato_get_by_id_usecase import ContatoGetByIdUseCase
from src.contato.domain.usecase.contato_get_by_doc_usecase import ContatoGetByDocUseCase
from src.contato.domain.usecase.contato_delete_usecase import ContatoDeleteUseCase


def create_contato():
    return handler.handle_usecase_insert(ContatoInsertUseCase)

def update_contato():
    return handler.handle_usecase_update(ContatoUpdateUseCase)

def get_all_contato():
    return handler.handle_usecase_execution(ContatoGetAllUseCase)

def get_by_id_contato(id:int):
    return handler.handle_usecase_execution(ContatoGetByIdUseCase, id)

def get_by_doc_contato(doc: str):
    return handler.handle_usecase_execution(ContatoGetByDocUseCase, doc)

def delete_contato(id):
    return handler.handle_usecase_delete(ContatoDeleteUseCase, id)
