"""
Aplicação web simples em Python usando Flask.
O usuário digita um número em uma tela no navegador e o sistema
exibe a contagem de 1 até o número digitado.

Como executar:
    1. Instale o Flask (se ainda não tiver):
       pip install flask

    2. Rode o arquivo:
       python app_contagem.py

    3. Abra o navegador em:
       http://127.0.0.1:5000
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

# ---------- Template HTML (embutido no próprio arquivo) ----------
TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Contagem até o número</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 60px auto;
            padding: 0 20px;
            color: #222;
        }
        h1 {
            font-size: 22px;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="number"] {
            padding: 8px;
            font-size: 16px;
            width: 150px;
        }
        button {
            padding: 8px 16px;
            font-size: 16px;
            margin-left: 8px;
            cursor: pointer;
        }
        .erro {
            color: #b00020;
        }
        .resultado {
            background: #f5f5f5;
            padding: 12px;
            border-radius: 6px;
            word-wrap: break-word;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <h1>Digite um número</h1>
    <form method="POST">
        <input type="number" name="valor" placeholder="Ex: 10" required
               value="{{ valor_digitado if valor_digitado is not none else '' }}">
        <button type="submit">Contar</button>
    </form>

    {% if erro %}
        <p class="erro">{{ erro }}</p>
    {% endif %}

    {% if resultado %}
        <div class="resultado">
            <strong>Contagem xpto de 1 até {{ valor_digitado }}:</strong><br>
            {{ resultado }}
        </div>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    valor_digitado = None

    if request.method == "POST":
        texto = request.form.get("valor", "")
        try:
            valor_digitado = int(texto)
            if valor_digitado < 1:
                erro = "Digite um número inteiro maior ou igual a 1."
            else:
                resultado = ", ".join(str(n) for n in range(1, valor_digitado + 1))
        except ValueError:
            erro = "Digite um número inteiro válido."

    return render_template_string(
        TEMPLATE, resultado=resultado, erro=erro, valor_digitado=valor_digitado
    )


if __name__ == "__main__":
    app.run(debug=True)
