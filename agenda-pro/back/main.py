# import asyncpg
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import datetime

# app = FastAPI()

# origins = [
#  "http://127.0.0.1:5500/",
#  "http://127.0.0.1:5500",
#  "http://localhost:5500/",
#  "http://localhost:5500"
#  "http://127.0.0.1:5500/front/index.html"
#  "http://127.0.0.1:5500/front/cadastro.html"
#  "http://127.0.0.1:5500/front/edicao.html"
# ]

# user="postgres"
# password="sql"
# database="agendateste"
# host="localhost"

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# async def criar_conexao_banco():
#     connection = await asyncpg.connect(user=user, password=password, database=database, host=host)
#     return connection


# @app.get("/teste")
# async def test_connection():
#     conn = await criar_conexao_banco()
#     await conn.close()
#     return {"message": "Conexao com sucesso!"}


# # CRUD de Clientes 

# @app.get("/clientes")
# async def get_clientes():
#     conn = await criar_conexao_banco()
#     linhas = await conn.fetch("SELECT * FROM clientes")
#     await conn.close()
#     clientes = []
#     for linha in linhas:
#         clientes.append(dict(linha))
#     return {"clientes": clientes}


# @app.get("/cliente/{cpf_cnpj}")
# async def get_cliente(cpf_cnpj: str):
#     conn = await criar_conexao_banco()
#     cliente = await conn.fetchrow("SELECT * FROM clientes WHERE cpf_cnpj = $1", cpf_cnpj)
#     await conn.close()
#     return {"cliente": dict(cliente)}


# @app.post("/cliente")
# async def create_cliente(cliente: dict):
#     conn = await criar_conexao_banco()
#     await conn.execute(
#         """INSERT INTO clientes (cpf_cnpj, nome, telefone, email, endereco) VALUES ($1, $2, $3, $4, $5)""",
#         cliente["cpf_cnpj"], cliente["nome"], cliente["telefone"], cliente["email"], cliente["endereco"]
#     )
#     await conn.close()
#     return {"message": "Cliente cadastrado com sucesso!"}


# @app.put("/cliente/{cpf_cnpj}")
# async def update_cliente(cpf_cnpj: str, cliente: dict):
#     conn = await criar_conexao_banco()
#     result = await conn.execute("""
#         UPDATE clientes
#         SET nome = $1, telefone = $2, email = $3, endereco = $4
#         WHERE cpf_cnpj = $5
#     """, cliente["nome"], cliente["telefone"], cliente["email"], cliente["endereco"], cpf_cnpj)
#     await conn.close()
#     if result == "UPDATE 1":
#         return {"message": f"Cliente atualizado com sucesso: {cpf_cnpj}"}
#     return {"message": "Cliente nao atualizado"}


# @app.delete("/cliente/{cpf_cnpj}")
# async def delete_cliente(cpf_cnpj: str):
#     conn = await criar_conexao_banco()
#     result = await conn.execute("DELETE FROM clientes WHERE cpf_cnpj = $1", cpf_cnpj)
#     await conn.close()
#     if result == "DELETE 1":
#         return {"message": f"Cliente deletado com sucesso! CPF/CNPJ: {cpf_cnpj}"}
#     return {"message": "Cliente não foi deletado"}


# # CRUD de Agendamentos

# @app.get("/agendamentos")
# async def get_agendamentos():
#     conn = await criar_conexao_banco()
#     linhas = await conn.fetch("SELECT * FROM agendamentos")
#     await conn.close()
#     agendamentos = []
#     for linha in linhas:
#         agendamentos.append(dict(linha))
#     return {"agendamentos": agendamentos}


# @app.get("/agendamento/{id}")
# async def get_agendamento(id: int):
#     conn = await criar_conexao_banco()
#     agendamento = await conn.fetchrow("SELECT * FROM agendamentos WHERE id = $1", id)
#     await conn.close()
#     return {"agendamento": dict(agendamento)}


# @app.post("/agendamento")
# async def create_agendamento(agendamento: dict):
#     conn = await criar_conexao_banco()

#     data_atendimento = datetime.datetime.strptime(agendamento["data_atendimento"], '%Y-%m-%dT%H:%M')
#     retorno = datetime.datetime.strptime(agendamento["retorno"], '%Y-%m-%dT%H:%M') if agendamento["retorno"] else None

#     await conn.execute(
#         """INSERT INTO agendamentos (cliente_cpf_cnpj, servico_id, data_atendimento, valor, retorno, status, observacoes) 
#            VALUES ($1, $2, $3, $4, $5, $6, $7)""",
#         agendamento["cliente_cpf_cnpj"], int(agendamento["servico_id"]), data_atendimento, 
#         agendamento["valor"], retorno, agendamento["status"], agendamento["observacoes"]
#     )
#     await conn.close()
#     return {"message": "Agendamento cadastrado com sucesso!"}


# @app.put("/agendamento/{id}")
# async def update_agendamento(id: int, agendamento: dict):
#     data_atendimento = datetime.datetime.strptime(agendamento["data_atendimento"], '%Y-%m-%d').date()
#     retorno = datetime.datetime.strptime(agendamento["retorno"], '%Y-%m-%d').date()

#     conn = await criar_conexao_banco()
#     result = await conn.execute("""
#         UPDATE agendamentos
#         SET cliente_cpf_cnpj = $1, servico_id = $2, data_atendimento = $3, valor = $4, retorno = $5
#         WHERE id = $6
#     """, agendamento["cliente_cpf_cnpj"], agendamento["servico_id"], data_atendimento, 
#        agendamento["valor"], retorno, id)
#     await conn.close()
#     if result == "UPDATE 1":
#         return {"message": f"Agendamento atualizado com sucesso: {id}"}
#     return {"message": "Agendamento nao atualizado"}


# @app.delete("/agendamento/{id}")
# async def delete_agendamento(id: int):
#     conn = await criar_conexao_banco()
#     result = await conn.execute("DELETE FROM agendamentos WHERE id = $1", id)
#     await conn.close()
#     if result == "DELETE 1":
#         return {"message": f"Agendamento deletado com sucesso! ID: {id}"}
#     return {"message": "Agendamento não foi deletado"}


# # CRUD de Serviços

# @app.get("/servicos")
# async def get_servicos():
#     conn = await criar_conexao_banco()
#     linhas = await conn.fetch("SELECT * FROM servicos")
#     await conn.close()
#     servicos = []
#     for linha in linhas:
#         servicos.append(dict(linha))
#     return {"servicos": servicos}


# @app.get("/servico/{id}")
# async def get_servico(id: int):
#     conn = await criar_conexao_banco()
#     servico = await conn.fetchrow("SELECT * FROM servicos WHERE id = $1", id)
#     await conn.close()
#     return {"servico": dict(servico)}


# @app.post("/servico")
# async def create_servico(servico: dict):
#     conn = await criar_conexao_banco()
#     await conn.execute(
#         """INSERT INTO servicos (descricao, valor) VALUES ($1, $2)""",
#         servico["descricao"], servico["valor"]
#     )
#     await conn.close()
#     return {"message": "Servico cadastrado com sucesso!"}


# @app.put("/servico/{id}")
# async def update_servico(id: int, servico: dict):
#     conn = await criar_conexao_banco()
#     result = await conn.execute("""
#         UPDATE servicos
#         SET descricao = $1, valor = $2
#         WHERE id = $3
#     """, servico["descricao"], servico["valor"], id)
#     await conn.close()
#     if result == "UPDATE 1":
#         return {"message": f"Servico atualizado com sucesso: {id}"}
#     return {"message": "Servico nao atualizado"}


# @app.delete("/servico/{id}")
# async def delete_servico(id: int):
#     conn = await criar_conexao_banco()
#     result = await conn.execute("DELETE FROM servicos WHERE id = $1", id)
#     await conn.close()
#     if result == "DELETE 1":
#         return {"message": f"Servico deletado com sucesso! ID: {id}"}
#     return {"message": "Servico não foi deletado"}

import asyncpg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()


origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user="postgres"
password="1312"
database="agendateste"
host="localhost"

async def criar_conexao_banco():
    connection = await asyncpg.connect(user=user, password=password, database=database, host=host)
    return connection


@app.get("/teste")
async def test_connection():
    conn = await criar_conexao_banco()
    await conn.close()
    return {"message": "Conexao com sucesso!"}


# CRUD de Agendamentos

@app.get("/agendamentos")
async def get_agendamentos():
    conn = await criar_conexao_banco()
    query = """
        SELECT 
            agendamentos.id, 
            clientes.nome AS cliente_nome, 
            servicos.descricao AS servico_nome, 
            agendamentos.data_atendimento, 
            agendamentos.valor, 
            agendamentos.retorno, 
            agendamentos.status, 
            agendamentos.observacoes
        FROM 
            agendamentos
        INNER JOIN 
            clientes ON agendamentos.cliente_cpf_cnpj = clientes.cpf_cnpj
        INNER JOIN 
            servicos ON agendamentos.servico_id = servicos.id
    """
    linhas = await conn.fetch(query)
    await conn.close()
    agendamentos = []
    for linha in linhas:
        agendamentos.append(dict(linha))
    return {"agendamentos": agendamentos}


@app.get("/agendamento/{id}")
async def get_agendamento(id: int):
    conn = await criar_conexao_banco()
    agendamento = await conn.fetchrow("SELECT * FROM agendamentos WHERE id = $1", id)
    print(agendamento)
    await conn.close()
    return {"agendamento": dict(agendamento)}


@app.post("/agendamento")
async def create_agendamento(agendamento: dict):
    conn = await criar_conexao_banco()
    if agendamento["data_atendimento"] is not None:
        data_atendimento = datetime.datetime.strptime(agendamento["data_atendimento"], '%Y-%m-%dT%H:%M')
    else:
        data_atendimento = None

    if agendamento.get("retorno") is not None:
        retorno = datetime.datetime.strptime(agendamento["retorno"], '%Y-%m-%dT%H:%M')
    else:
        retorno = None

    await conn.execute(
        """INSERT INTO agendamentos (cliente_cpf_cnpj, servico_id, data_atendimento, valor, retorno, status, observacoes) 
           VALUES ($1, $2, $3, $4, $5, $6, $7)""",
        agendamento["cliente_cpf_cnpj"], int(agendamento["servico_id"]), data_atendimento, 
        agendamento["valor"], retorno, agendamento["status"], agendamento["observacoes"]
    )
    await conn.close()
    return {"message": "Agendamento cadastrado com sucesso!"}


@app.put("/agendamento/{id}")
async def update_agendamento(id: int, agendamento: dict):
    data_atendimento = datetime.datetime.strptime(agendamento["data_atendimento"], '%Y-%m-%dT%H:%M')
    retorno = datetime.datetime.strptime(agendamento["retorno"], '%Y-%m-%dT%H:%M') if agendamento["retorno"] else None

    conn = await criar_conexao_banco()
    result = await conn.execute("""
        UPDATE agendamentos
        SET cliente_cpf_cnpj = $1, servico_id = $2, data_atendimento = $3, valor = $4, retorno = $5
        WHERE id = $6
    """, agendamento["cliente_cpf_cnpj"], int(agendamento["servico_id"]), data_atendimento, 
       agendamento["valor"], retorno, id)
    await conn.close()
    if result == "UPDATE 1":
        return {"message": f"Agendamento atualizado com sucesso: {id}"}
    return {"message": "Agendamento nao atualizado"}


@app.delete("/agendamento/{id}")
async def delete_agendamento(id: int):
    conn = await criar_conexao_banco()
    result = await conn.execute("DELETE FROM agendamentos WHERE id = $1", id)
    await conn.close()
    if result == "DELETE 1":
        return {"message": f"Agendamento deletado com sucesso! ID: {id}"}
    return {"message": "Agendamento não foi deletado"}


# GET de Serviços

@app.get("/servicos")
async def get_servicos():
    conn = await criar_conexao_banco()
    linhas = await conn.fetch("SELECT * FROM servicos")
    await conn.close()
    servicos = []
    for linha in linhas:
        servicos.append(dict(linha))
    return {"servicos": servicos}


@app.get("/servico/{id}")
async def get_servico(id: int):
    conn = await criar_conexao_banco()
    servico = await conn.fetchrow("SELECT * FROM servicos WHERE id = $1", id)
    await conn.close()
    return {"servico": dict(servico)}


# GET de Clientes 

@app.get("/clientes")
async def get_clientes():
    conn = await criar_conexao_banco()
    linhas = await conn.fetch("SELECT * FROM clientes")
    await conn.close()
    clientes = []
    for linha in linhas:
        clientes.append(dict(linha))
    return {"clientes": clientes}


@app.get("/cliente/{cpf_cnpj}")
async def get_cliente(cpf_cnpj: str):
    conn = await criar_conexao_banco()
    cliente = await conn.fetchrow("SELECT * FROM clientes WHERE cpf_cnpj = $1", cpf_cnpj)
    await conn.close()
    return {"cliente": dict(cliente)}
