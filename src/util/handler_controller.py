from werkzeug.exceptions import BadRequest
from flask import jsonify

def handle_usecase_execution(usecase, *args, http_status=200, **kwargs):
    try:
        result = usecase(*args, **kwargs).execute()
        return result, http_status
    except BadRequest:
        return jsonify({"error": "Requisição inválida. Verifique o formato dos dados enviados."}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Erro ao executar {usecase.__name__}:", e)
        return jsonify({"error": "Erro interno do servidor", "message": str(e)}), 500
    
def handle_usecase_insert(usecase, *args, **kwargs):
    try:
        id = usecase(*args, **kwargs).execute()
        return jsonify({"id": id['id']}), 201  
    except BadRequest:
        return jsonify({"error": "Requisição inválida. Verifique o formato dos dados enviados."}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Erro ao executar {usecase.__name__}:", e)
        return jsonify({"error": "Erro interno do servidor", "message": str(e)}), 500
    
def handle_usecase_update(usecase, *args, **kwargs):
    try:
        flag = usecase(*args, **kwargs).execute()
        if not flag:
            return jsonify({"error": f"Erro ao tentar atualizar o {usecase.__name__}!"}), 404
        return jsonify({"menssage": "Registro atualizado com sucesso."}), 202
    except BadRequest:
        return jsonify({"error": "Requisição inválida. Verifique o formato dos dados enviados."}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Erro ao executar {usecase.__name__}:", e)
        return jsonify({"error": "Erro interno do servidor", "message": str(e)}), 500
    
def handle_usecase_delete(usecase, *args, **kwargs):
    try:
        flag = usecase(*args, **kwargs).execute()
        if not flag:
            return jsonify({"error": f"Erro ao tentar excluir o {usecase.__name__}!"}), 404
        return jsonify({"menssage": "Registro excluido com sucesso."}), 202
    except BadRequest:
         return jsonify({"error": "Requisição inválida. Verifique o formato dos dados enviados."}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Erro ao executar {usecase.__name__}:", e)
        return jsonify({"error": "Erro interno do servidor", "message": str(e)}), 500