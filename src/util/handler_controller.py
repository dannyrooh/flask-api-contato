from werkzeug.exceptions import BadRequest
from flask import jsonify
from http import HTTPStatus
from .errors import DeleteError, NotFoundError

def handle_exceptions(usecase, e):

    if isinstance(e, BadRequest):
        return jsonify({"error": "Requisição inválida."}), HTTPStatus.BAD_REQUEST
    elif isinstance(e, ValueError):
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
    elif isinstance(e, NotFoundError):
        return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND
    else:
        print(f"Erro ao executar {usecase.__name__}:", e)
        return jsonify({"error": "Erro interno do servidor", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

def handle_usecase_execution(usecase, *args, http_status=HTTPStatus.OK, **kwargs):
    try:
        result = usecase(*args, **kwargs).execute()
        return result, http_status
    except Exception as e:
        return handle_exceptions(usecase, e)
    
def handle_usecase_insert(usecase, *args, **kwargs):
    try:
        id = usecase(*args, **kwargs).execute()
        return jsonify({"id": id['id']}), HTTPStatus.CREATED
    except Exception as e:
        return handle_exceptions(usecase, e)
    
def handle_usecase_update(usecase, *args, **kwargs):
    try:
        flag = usecase(*args, **kwargs).execute()
        if not flag:
            return jsonify({"error": f"Erro ao tentar atualizar o {usecase.__name__}!"}), HTTPStatus.NOT_FOUND
        return jsonify({"menssage": "Registro atualizado com sucesso."}), HTTPStatus.ACCEPTED
    except Exception as e:
        return handle_exceptions(usecase, e)
    
def handle_usecase_delete(usecase, *args, **kwargs):
    try:
        flag = usecase(*args, **kwargs).execute()
        if not flag:
            return jsonify({"error": f"Erro ao tentar excluir o {usecase.__name__}!"}), HTTPStatus.NOT_FOUND
        return '', HTTPStatus.NO_CONTENT
    except DeleteError as e:
        return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return handle_exceptions(usecase, e)