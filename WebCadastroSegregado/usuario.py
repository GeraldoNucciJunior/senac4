"""
Blueprint de Cadastro de Usuário
---------------------------------
Contém as rotas relacionadas ao cadastro de usuário (código, nome).
"""

from flask import Blueprint, render_template_string, request, redirect, url_for

usuario_bp = Blueprint("usuario", __name__)

# "Banco de dados" em memória
usuarios = []

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


@usuario_bp.route("/usuarios", methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        codigo = request.form.get("codigo", "").strip()
        nome = request.form.get("nome", "").strip()
        if codigo and nome:
            usuarios.append({"codigo": codigo, "nome": nome})
        return redirect(url_for("usuario.cadastro_usuario"))

    # Importa o style do módulo principal (evita duplicar CSS)
    from app import BASE_STYLE
    return render_template_string(USUARIO_TEMPLATE, style=BASE_STYLE, usuarios=usuarios)
