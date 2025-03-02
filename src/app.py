import os

from .swagger_namespace import bootstrap_swagger
from . import create_app # from __init__ file


app = create_app(os.getenv("CONFIG_MODE"))

# # Hello World!
# @app.route('/')
# def hello():
#       return "Hello World!"

from src.contato.entrypoint import  contato_entrypoint


bootstrap_swagger(app)


if __name__ == "__main__":
      app.run()