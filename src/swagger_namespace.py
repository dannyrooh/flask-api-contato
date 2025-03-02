from src.configs.swagger_config import api_swagger
from src.contato.entrypoint.contato_swagger import ns_contato


def bootstrap_swagger(app):
    api_swagger.init_app(app)

    api_swagger.add_namespace(ns_contato)