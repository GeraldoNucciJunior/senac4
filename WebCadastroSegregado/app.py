"""
Aplicação Web em Python (Flask) - Arquivo Principal
------------------------------------------------------
Junta os blueprints de usuário e produto e sobe o servidor.
Tela inicial com menu apontando para:
  - Cadastro de Usuário (usuario.py)
  - Cadastro de Produto (produto.py)

Como executar:
    pip install flask
    python app.py

Depois acesse: http://127.0.0.1:5000
"""

from flask import Flask, render_template_string

from usuario import usuario_bp
from produto import produto_bp

app = Flask(__name__)

# Registra os blueprints (rotas separadas em outros arquivos)
app.register_blueprint(usuario_bp)
app.register_blueprint(produto_bp)

# ---------------------------------------------------------------------------
# Estilo compartilhado (usado também pelos templates de usuario.py e produto.py)
# ---------------------------------------------------------------------------

BASE_STYLE = """
<style>
    body {
        font-family: Arial, Helvetica, sans-serif;
        background-color: #f4f6f8;
        margin: 0;
        padding: 0;
    }
    header {
        background-color: #2c3e50;
        color: #fff;
        padding: 16px 24px;
    }
    header h1 { margin: 0; font-size: 22px; }
    nav a {
        color: #fff;
        text-decoration: none;
        margin-right: 16px;
        font-size: 14px;
    }
    nav a:hover { text-decoration: underline; }
    .container {
        max-width: 700px;
        margin: 30px auto;
        background: #fff;
        padding: 24px;
        border-radius: 8px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.1);
    }
    .menu-card {
        display: block;
        padding: 20px;
        margin-bottom: 16px;
        background: #ecf0f1;
        border-radius: 6px;
        text-decoration: none;
        color: #2c3e50;
        font-size: 18px;
        transition: background 0.2s;
    }
    .menu-card:hover { background: #dfe6e9; }
    form { margin-top: 16px; }
    label { display: block; margin-top: 12px; font-weight: bold; font-size: 14px; }
    input[type=text], input[type=number] {
        width: 100%;
        padding: 8px;
        margin-top: 4px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    button {
        margin-top: 18px;
        background-color: #2c3e50;
        color: #fff;
        border: none;
        padding: 10px 18px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
    }
    button:hover { background-color: #1a252f; }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 24px;
    }
    th, td {
        text-align: left;
        padding: 8px;
        border-bottom: 1px solid #ddd;
        font-size: 14px;
    }
    th { background-color: #ecf0f1; }
</style>
"""

MENU_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Cadastros</title>
    {{ style|safe }}
</head>
<body>
    <header>
        <h1>Sistema de Cadastros</h1>
    </header>
    <div class="container">
        <h2>Menu Principal</h2>
        <a class="menu-card" href="{{ url_for('usuario.cadastro_usuario') }}">👤 Cadastro de Usuário</a>
        <a class="menu-card" href="{{ url_for('produto.cadastro_produto') }}">📦 Cadastro de Produto</a>
    </div>
</body>
</html>
"""


@app.route("/")
def menu():
    return render_template_string(MENU_TEMPLATE, style=BASE_STYLE)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
