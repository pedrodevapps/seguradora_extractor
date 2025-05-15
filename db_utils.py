import sqlite3

def init_db():
    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT, cpf TEXT, rg TEXT, nascimento TEXT, sexo TEXT, estado_civil TEXT,
        endereco TEXT, cep TEXT, cidade TEXT, estado TEXT,
        telefone TEXT, celular TEXT, email TEXT, observacoes TEXT
    )''')
    conn.commit()
    conn.close()

def save_to_db(data):
    init_db()
    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()
    c.execute('''INSERT INTO clientes (nome, cpf, rg, nascimento, sexo, estado_civil,
        endereco, cep, cidade, estado, telefone, celular, email, observacoes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (data["nome"], data["cpf"], data["rg"], data["nascimento"], data["sexo"],
         data["estado_civil"], data["endereco"], data["cep"], data["cidade"], data["estado"],
         data["telefone"], data["celular"], data["email"], data["observacoes"]))
    conn.commit()
    conn.close()