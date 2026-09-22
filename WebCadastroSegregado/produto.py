"""
Blueprint de Cadastro de Produto
----------------------------------
Contém as rotas relacionadas ao cadastro de produto (código, nome, preço).
"""

from flask import Blueprint, render_template_string, request, redirect, url_for

produto_bp = Blueprint("produto", __name__)

# "Banco de dados" em memória
produtos = []

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


@produto_bp.route("/produtos", methods=["GET", "POST"])
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
        return redirect(url_for("produto.cadastro_produto"))

    # Importa o style do módulo principal (evita duplicar CSS)
    from app import BASE_STYLE
    return render_template_string(PRODUTO_TEMPLATE, style=BASE_STYLE, produtos=produtos)
