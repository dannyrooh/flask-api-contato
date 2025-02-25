from flask import request,jsonify

from src.util.cpf_cnpj_util import CpfCnpjUtil

class ContatoEntityInsert:
    def __init__(self):
        self.ident = ''
        self.nome = ''
        self.codigo = ''
        self.doc = ''
     
    def load_from_request(self):
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        self.ident = data.get('ident')
        self.nome = data.get('nome')
        self.codigo = data.get('codigo')
        self.doc = data.get('doc')

        if not self.ident and self.nome:
            self.ident = self.nome.split()[0]

        return self

    def validate(self):
        data = {'nome': self.nome, 'doc': self.doc}
        required_fields = [ 'nome', 'doc']
        missing_fields = [field for field in required_fields if not data.get(field)]

        if missing_fields:
            return jsonify({"error": "Campos obrigatórios ausentes", "missing_fields": missing_fields}), 400
        
        doc = CpfCnpjUtil(self.doc)
        if doc.validate():
            self.doc = doc.doc
        else:
            return jsonify({"error": "Cnpj/Cpf com formato inválido", "missing_fields": self.doc}), 400

        return self