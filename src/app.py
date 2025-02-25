import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# App Initialization
from . import create_app # from __init__ file
app = create_app(os.getenv("CONFIG_MODE"))

# Hello World!
@app.route('/')
def hello():
      return "Hello World!"

from src.contato.entrypoint import  contato_entrypoint

if __name__ == "__main__":
      app.run()