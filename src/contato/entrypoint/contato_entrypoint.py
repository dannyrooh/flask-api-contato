from src.app import app
from src.contato.entrypoint import contato_controller as controller

@app.route("/contato", methods=['POST'])
def create_contato():
    return controller.create_contato()

@app.route("/contato", methods=['PUT'])
def update_contato():
    return controller.update_contato()

@app.route("/contato/<int:id>", methods=['DELETE'])
def delete_contato(id):
    return controller.delete_contato(id)    

@app.route("/contato", methods=['GET'])
def get_all_contato():
    return controller.get_all_contato()

@app.route("/contato/<int:id>", methods=['GET'])
def get_by_id_contato(id):
    return controller.get_by_id_contato(id)    

@app.route("/contato/doc/<string:doc>", methods=['GET'])
def get_by_doc_contato(doc):
    return controller.get_by_doc_contato(doc)

