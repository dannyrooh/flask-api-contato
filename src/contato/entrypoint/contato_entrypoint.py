from flask import request
from src.app import app
from src.contato.entrypoint import contato_controller as controller

@app.route("/contato", methods=['GET', 'POST', 'PUT'])
def contato_entrypoint():
    if request.method == 'GET': return controller.get_all_contato()
    if request.method == 'POST': return controller.create_contato()
    if request.method == 'PUT': return controller.update_contato()
    else: return 'Method is Not Allowed'

@app.route("/contato/<int:id>", methods=['GET'])
def contato_get_by_id(id):
    return controller.get_by_id_contato(id)    

@app.route("/contato/doc/<string:doc>", methods=['GET'])
def contato_get_by_doc(doc):
    return controller.get_by_doc_contato(doc)

@app.route("/contato/<int:id>", methods=['DELETE'])
def entrypoint_contato_del_by_id(id):
    return controller.delete_contato(id)    