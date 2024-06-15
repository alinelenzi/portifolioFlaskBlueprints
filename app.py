
from flask import Flask, Blueprint, render_template

# Importei a função Blueprint da biblioteca Flask e criei uma instância dela

app= Flask(__name__)
bp = Blueprint('app', __name__)

# Agora defini minhas rotas, funções de vizualizações e as registrei no blueprint usando o bp.route

@bp.route('/')
@bp.route('/index')
def index():
    return render_template("index.html")

@bp.route('/sobre')
def sobre():
    return render_template("sobre.html")

@bp.route('/curriculo')
def curriculo():
    return render_template("curriculo.html")

@bp.route('/projetos')
def projetos():
    return render_template("projetos.html")

# Pega os dados do blueprint da aplicação (nome do app e as rotas) e registra dentro do app do Flask

app.register_blueprint(bp)

# Agora ao executar o aplicativo, ele incluirá as rotas definidas no blueprint.

if __name__ == '__main__':
    app.run(debug=True)

