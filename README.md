
# Executar a aplicação

* windows
    set PYTHONPATH=src
    flask run
* linux
    export PYTHONPATH=src
    flask run



flask --app app.py  run  --debug    

ou

$env:FLASK_APP = ".\src\app.py"; flask run --debug