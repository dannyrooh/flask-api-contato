from flask import request
from src.app import app
from src.contato.entrypoint.contato_controller import create_contato, get_all_contato, get_by_id_contato, update_contato, delete_contato, get_by_doc_contato

@app.route("/contato", methods=['GET', 'POST', 'PUT'])
def contato_entrypoint():
    if request.method == 'GET': return get_all_contato()
    if request.method == 'POST': return create_contato()
    if request.method == 'PUT': return update_contato()
    else: return 'Method is Not Allowed'

@app.route("/contato/<int:id>", methods=['GET'])
def contato_get_by_id(id):
    return get_by_id_contato(id)    

@app.route("/contato/doc/<string:doc>", methods=['GET'])
def contato_get_by_doc(doc):
    return get_by_doc_contato(doc)

@app.route("/contato/<int:id>", methods=['DELETE'])
def contato_del_by_id(id):
    return delete_contato(id)    