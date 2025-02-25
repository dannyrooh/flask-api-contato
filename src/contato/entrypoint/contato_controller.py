from flask import jsonify, request
from werkzeug.exceptions import BadRequest

from src.contato.domain.entity.contato_entity_insert import ContatoEntityInsert
from src.contato.domain.entity.contato_entity_update import ContatoEntityUpdate
from src.contato.domain.provider.contato_provider import ContatoProvider

def create_contato():
    try:
        contato_entity = ContatoEntityInsert()
        contato_entity.load_from_request()
        contato_entity.validate()

        provider = ContatoProvider()

        contato: str = provider.get_contato_by_doc(contato_entity.doc)
        if contato:
            return jsonify({"error": f'Contato já cadastrado {contato}'}), 400

        new_contato = provider.create_contato(contato_entity)

        return jsonify({"message": "Contato criado com sucesso", "id": new_contato.con_id}), 201  

    except BadRequest:
        return jsonify({"error": "Requisição inválida. Verifique o formato dos dados enviados."}), 400
    except Exception as e:
        print("Erro ao criar contato:", e)
        return jsonify({"error": "Erro interno do servidor", "message": str(e)}), 500
    
def update_contato():
    try:
        contato_entity = ContatoEntityUpdate()
        contato_entity.load_from_request()
        contato_entity.validate()

        provider = ContatoProvider()

        contato = provider.get_contato_by_doc(contato_entity.doc)
        if contato:
            if contato['id'] != contato_entity.id:
                return jsonify({"error": f'Existe um outro Contato com o CPF/CNPJ cadastrado {contato["doc"]}'}), 400

        new_contato = provider.update_contato(contato_entity)

        if not new_contato:
            return jsonify({"error": "Erro ao tentar atualizar o contato!"}), 404

        return jsonify({"message": "Contato atualizado com sucesso"}), 200  

    except BadRequest:
        return jsonify({"error": "Requisição inválida. Verifique o formato dos dados enviados."}), 400
    except Exception as e:
        print("Erro ao criar contato:", e)
        return jsonify({"error": "Erro interno do servidor", "message": str(e)}), 500

def get_all_contato():
    all = ContatoProvider().get_all_contato()
    return jsonify(all)

def get_by_id_contato(id:int):
    contato = ContatoProvider().get_contato_by_id(id)
    if not contato:
        return jsonify({"error": "Contato não encontrado"}), 404
    return jsonify(contato)

def get_by_doc_contato(doc:str):
    contato = ContatoProvider().get_contato_by_doc(doc)
    if not contato:
        return jsonify({"error": "Contato não encontrado"}), 404
    return jsonify(contato)    

def delete_contato(id):
    return {'message': f'Delete Contato {id}'}