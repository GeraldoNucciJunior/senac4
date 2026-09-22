import os
os.system('cls' if os.name == 'nt' else 'clear')

db_congig = dict(
    host="localhost",
    porta=3306,
    usuario="root",
    senha="senha@126"
)

print (f"Conectando ao banco de dados {db_congig['host']} na porta {db_congig['porta']} com o usuário {db_congig['usuario']}.")
