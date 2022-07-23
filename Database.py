import sqlite3, random, string

def gerarid(tamanho):
    gerado = ""
    letras = string.ascii_letters
    numeros = "1","2","3","4","5","6","7","8","9","0"
    for __ in range(tamanho):
        opcoes = "L","N"
        opcao = random.choice(opcoes)
        if(opcao == "L"):
            gerado += random.choice(letras)
        else:
            gerado += random.choice(numeros)
    return gerado

#Banco de dados puramente.
def conectar():
    return sqlite3.connect("assets/dados.db")

def criarpadrao():
    db = conectar()
    db.executescript("""PRAGMA journal_mode=WAL""")
    db.executescript(""" CREATE TABLE IF NOT EXISTS LISTAS(ID TEXT PRIMARY KEY NOT NULL, TITULO TEXT NOT NULL, LINK TEXT NOT NULL, LOCAL TEXT NOT NULL, GRUPO_ID TEXT NOT NULL); """)
    db.executescript(""" CREATE TABLE IF NOT EXISTS LISTAS_USADAS(ID TEXT PRIMARY KEY NOT NULL, LOCAL TEXT NOT NULL, GRUPO_ID TEXT NOT NULL);""")
    db.executescript(""" CREATE TABLE IF NOT EXISTS GRUPOS(GRUPO_ID TEXT PRIMARY KEY NOT NULL, MODO TEXT NOT NULL, BANIDO TEXT NOT NULL);""")
    db.executescript(""" CREATE TABLE IF NOT EXISTS USERS(USER_ID TEXT PRIMARY KEY, BANIDO TEXT NOT NULL);""")
    db.commit()
    db.close()

#Banco de dados: gerenciador de grupo config -> get.
def get_modo(grupo_id):
    db = conectar()
    modo = db.execute(f"""SELECT MODO FROM GRUPOS WHERE GRUPO_ID='{grupo_id}'""").fetchone()[0]
    db.commit()
    db.close()
    return modo

#Banco de dados: gerenciador de grupo config -> post.
def post_modo(grupo_id, modo):
    db = conectar()
    db.executescript(f"""UPDATE GRUPOS SET MODO='{modo}' WHERE GRUPO_ID='{grupo_id}'""")
    db.commit()
    db.close()

def post_grupo(grupo_id):
    db = conectar()
    try:
        db.executescript(f""" INSERT INTO GRUPOS(GRUPO_ID, MODO, BANIDO) VALUES ('{grupo_id}','video','false');""")
    except:
        pass
    db.commit()
    db.close()

#Banco de dados: gerenciador de listas -> get.
def get_lista(grupo_id):
    db = conectar()
    dados = db.execute(f"""SELECT * FROM LISTAS WHERE GRUPO_ID='{grupo_id}'""").fetchall()[0]
    id = dados[0]
    local = dados[3]
    grupo_id = dados[4]
    db.executescript(f"""INSERT INTO LISTAS_USADAS(ID, LOCAL, GRUPO_ID) VALUES ('{id}','{local}','{grupo_id}');""")
    db.executescript(f"""DELETE FROM LISTAS WHERE ID='{id}'""")
    db.commit()
    db.close()
    return dados

def get_listas(grupo_id):
    db = conectar()
    dados = db.execute(f"""SELECT * FROM LISTAS WHERE GRUPO_ID='{grupo_id}'""").fetchall()
    db.commit()
    db.close()
    return dados

def get_usada(grupo_id):
    db = conectar()
    dados = db.execute(f"""SELECT * FROM LISTAS_USADAS WHERE GRUPO_ID='{grupo_id}'""").fetchall()[0]
    id = dados[0]
    db.executescript(f"""DELETE FROM LISTAS_USADAS WHERE ID='{id}'""")
    db.commit()
    db.close()
    return dados

#Banco de dados: gerenciador de listas -> checagem.
def vazia(grupo_id):
    db = conectar()
    try:
        dados = db.execute(f"""SELECT * FROM LISTAS WHERE GRUPO_ID='{grupo_id}'""").fetchall()[0]
        db.commit()
        db.close()
        return False
    except:
        return True

def banido(grupo_id):
    db = conectar()
    status = db.execute(f"""SELECT BANIDO FROM GRUPOS WHERE GRUPO_ID='{grupo_id}'""").fetchall()[0]
    db.commit()
    db.close()
    if(status == "true"):
        return True
    else:
        return False

def permitido(admin, user_id):
    db = conectar()
    try:
        status = db.execute(f"""SELECT BANIDO FROM USERS WHERE USER_ID='{user_id}'""").fetchone()[0]
    except:
        status = "true"
    db.commit()
    db.close()
    if(admin==True or status=="false"):
        return True
    else:
        return False

#Banco de dados: gerenciador de listas -> post.
def post_lista(titulo, link, local, grupo_id):
    db = conectar()
    id = gerarid(50)
    db.executescript(f"""INSERT INTO LISTAS(ID, TITULO, LINK, LOCAL, GRUPO_ID) VALUES ('{id}','{titulo}','{link}','{local}','{grupo_id}');""")
    db.commit()
    db.close()

#Banco de dados: gerenciador de users -> post.
def post_user(user_id):
    db = conectar()
    db.executescript(f"""INSERT INTO USERS(USER_ID, BANIDO) VALUES ('{user_id}','false');""")
    db.commit()
    db.close()

#Banco de dados: gerenciador de users -> delete.
def delete_user(user_id):
    db = conectar()
    db.executescript(f"""DELETE FROM USERS WHERE USER_ID='{user_id}'""")
    db.commit()
    db.close()