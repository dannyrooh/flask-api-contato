from http import HTTPStatus

from flask_restx import Resource, Namespace, fields, reqparse

from src.configs.swagger_config import api_swagger as api

ns_contato = Namespace('/', description='Contato CRUD')


get_model_contato = api.model('Contato', {
    'id': fields.Integer,
    'codigo': fields.Integer,
    'doc': fields.String,
    'nome': fields.String,
    'ident': fields.String,
    'root': fields.Integer,
    'tipo': fields.Integer,
    'hash': fields.String
})

result_contato_model_id = api.model('ContatoId', {
    'id': fields.Integer
})

@ns_contato.route('/contato')
class ContatoResource(Resource):


    parserPostContato = reqparse.RequestParser()
    parserPostContato.add_argument('ident', type=str, location='json', required=False) 
    parserPostContato.add_argument('nome', type=str, location='json', required=False)
    parserPostContato.add_argument('codigo', type=int, location='json', required=False) 
    parserPostContato.add_argument('doc', type=str, location='json', required=True, help='CPF ou CNPJ') 
    

    @ns_contato.doc('create_contato')
    @api.doc(parser=parserPostContato)
    @api.marshal_with(result_contato_model_id, code=HTTPStatus.CREATED)
    @ns_contato.response(HTTPStatus.CREATED, 'Contato criado')
    @ns_contato.response(HTTPStatus.NOT_FOUND, 'Contato não encontrado')
    @ns_contato.response(HTTPStatus.BAD_REQUEST, 'Requisição inválida')
    @ns_contato.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Erro interno do servidor')
    def post( self):
        """Adiciona um novo contato"""
        return [], HTTPStatus.CREATED

    parserPutContato = reqparse.RequestParser()
    parserPutContato.add_argument('id', type=int, location='json') 
    parserPutContato.add_argument('ident', type=str, location='json') 
    parserPutContato.add_argument('nome', type=str, location='json') 
    parserPutContato.add_argument('codigo', type=int, location='json') 
    parserPutContato.add_argument('doc', type=str, location='json') 

    @ns_contato.doc('update_contato')
    @api.doc(parser=parserPutContato)
    @ns_contato.response(HTTPStatus.NO_CONTENT, 'Contato atualizado')
    @ns_contato.response(HTTPStatus.NOT_FOUND, 'Contato não encontrado')
    @ns_contato.response(HTTPStatus.BAD_REQUEST, 'Requisição inválida')
    @ns_contato.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Erro interno do servidor')    
    def put(self):
        """Altera um contato existente"""
        return []
    
    @ns_contato.doc('get_all_contato')
    @api.marshal_with(get_model_contato)
    def get(self):
        """Retorna a lista de contatos"""
        return []


@ns_contato.route('/contato/<int:id>')
class ContatoIdResource(Resource):

    @ns_contato.doc('get_by_id_contato')
    @api.marshal_with(get_model_contato)
    @ns_contato.response(HTTPStatus.OK, 'Contato encontrado')
    @ns_contato.response(HTTPStatus.NOT_FOUND, 'Contato não encontrado')
    @ns_contato.response(HTTPStatus.BAD_REQUEST, 'Requisição inválida')
    @ns_contato.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Erro interno do servidor')
    def get(self, id):
        """Retorna um contato pelo id"""
        return [], HTTPStatus.OK
    
    @ns_contato.doc('delete_contato')
    @ns_contato.response(HTTPStatus.NO_CONTENT, 'Contato excluido')
    @ns_contato.response(HTTPStatus.NOT_FOUND, 'Contato não encontrado')
    @ns_contato.response(HTTPStatus.BAD_REQUEST, 'Requisição inválida')
    @ns_contato.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Erro interno do servidor')
    def delete(self, id):
        """Exclui um contato pelo id"""
        return '', HTTPStatus.NO_CONTENT
    

@ns_contato.route('/contato/doc/<string:doc>')
class ContatoDocResource(Resource):

    @ns_contato.doc('get_by_doc_contato')
    @api.marshal_with(get_model_contato)
    @ns_contato.response(HTTPStatus.OK, 'Contato encontrado')
    @ns_contato.response(HTTPStatus.NOT_FOUND, 'Contato não encontrado')
    @ns_contato.response(HTTPStatus.BAD_REQUEST, 'CNPJ ou CPF inválido | Requisição inválida')
    @ns_contato.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Erro interno do servidor')
    def get(self, doc):
        """Retorna um contato pelo Doc (CNPJ ou CPF)"""
        return [], HTTPStatus.OK    