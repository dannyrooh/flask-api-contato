from flask import request,jsonify

from src.util.cpf_cnpj_util import CpfCnpjUtil

class ContatoEntity:
    def __init__(self):

        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        self.id = data.get('id', None)
        self.ident = data.get('ident', None)
        self.nome = data.get('nome',None)
        self.codigo = data.get('codigo',None)
        self.doc = data.get('doc',None)

        if not self.ident and self.nome:
            self.ident = self.nome.split()[0]

        self.cpfCnpjUtil = CpfCnpjUtil(self.doc)
        self.doc = self.cpfCnpjUtil.unformat()

    def validate(self):
        data = {'nome': self.nome, 'doc': self.doc}
        required_fields = [ 'nome', 'doc']
        missing_fields = [field for field in required_fields if not data.get(field)]

        if missing_fields:
            raise ValueError(f"Campos obrigatórios ausentes: {', '.join(missing_fields)}")
        
        if not self.cpfCnpjUtil.validate():
            raise ValueError("Cnpj/Cpf com formato inválido")