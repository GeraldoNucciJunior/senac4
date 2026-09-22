"""
Aplicação Web em Python (Flask)
--------------------------------
Tela inicial com menu apontando para:
  - Cadastro de Usuário (código, nome)
  - Cadastro de Produto (código, nome, preço)

Como executar:
    pip install flask
    python app.py

Depois acesse: http://127.0.0.1:5000
"""

from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# "Bancos de dados" em memória (listas de dicionários)
usuarios = []
produtos = []

# ---------------------------------------------------------------------------
# Templates (usando render_template_string para manter tudo em um único arquivo)
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
        <a class="menu-card" href="{{ url_for('cadastro_usuario') }}">👤 Cadastro de Usuário</a>
        <a class="menu-card" href="{{ url_for('cadastro_produto') }}">📦 Cadastro de Produto</a>
    </div>
</body>
</html>
"""

USUARIO_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Usuário</title>
    {{ style|safe }}
</head>
<body>
    <header>
        <h1>Cadastro de Usuário</h1>
        <nav><a href="{{ url_for('menu') }}">&larr; Voltar ao Menu</a></nav>
    </header>
    <div class="container">
        <form method="POST">
            <label for="codigo">Código</label>
            <input type="text" id="codigo" name="codigo" required>

            <label for="nome">Nome</label>
            <input type="text" id="nome" name="nome" required>

            <button type="submit">Salvar</button>
        </form>

        <table>
            <thead>
                <tr><th>Código</th><th>Nome</th></tr>
            </thead>
            <tbody>
                {% for u in usuarios %}
                <tr><td>{{ u.codigo }}</td><td>{{ u.nome }}</td></tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

PRODUTO_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Produto</title>
    {{ style|safe }}
</head>
<body>
    <header>
        <h1>Cadastro de Produto</h1>
        <nav><a href="{{ url_for('menu') }}">&larr; Voltar ao Menu</a></nav>
    </header>
    <div class="container">
        <form method="POST">
            <label for="codigo">Código</label>
            <input type="text" id="codigo" name="codigo" required>

            <label for="nome">Nome</label>
            <input type="text" id="nome" name="nome" required>

            <label for="preco">Preço</label>
            <input type="number" id="preco" name="preco" step="0.01" min="0" required>

            <button type="submit">Salvar</button>
        </form>

        <table>
            <thead>
                <tr><th>Código</th><th>Nome</th><th>Preço</th></tr>
            </thead>
            <tbody>
                {% for p in produtos %}
                <tr><td>{{ p.codigo }}</td><td>{{ p.nome }}</td><td>R$ {{ '%.2f'|format(p.preco) }}</td></tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Rotas
# ---------------------------------------------------------------------------

@app.route("/")
def menu():
    return render_template_string(MENU_TEMPLATE, style=BASE_STYLE)


@app.route("/usuarios", methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        codigo = request.form.get("codigo", "").strip()
        nome = request.form.get("nome", "").strip()
        if codigo and nome:
            usuarios.append({"codigo": codigo, "nome": nome})
        return redirect(url_for("cadastro_usuario"))
    return render_template_string(USUARIO_TEMPLATE, style=BASE_STYLE, usuarios=usuarios)


@app.route("/produtos", methods=["GET", "POST"])
def cadastro_produto():
    if request.method == "POST":
        codigo = request.form.get("codigo", "").strip()
        nome = request.form.get("nome", "").strip()
        preco_raw = request.form.get("preco", "0").strip()
        try:
            preco = float(preco_raw)
        except ValueError:
            preco = 0.0
        if codigo and nome:
            produtos.append({"codigo": codigo, "nome": nome, "preco": preco})
        return redirect(url_for("cadastro_produto"))
    return render_template_string(PRODUTO_TEMPLATE, style=BASE_STYLE, produtos=produtos)


if __name__ == "__main__":
    app.run(debug=True)
