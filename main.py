from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
import os

caminho_env = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    ".env"
)

load_dotenv(caminho_env)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Cliente Supabase inicializado!")

app = FastAPI()

@app.get("/clientes")
def listar_clientes_banco():
    resposta = (
    supabase
    .table("clientes")
    .select("*")
    .limit(5)
    .execute()
)

    return resposta.data


clientes = []


def cadastrar_cliente(nome: str, cpf: str, telefone: str):

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return "Cliente já cadastrado!"

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone
    }

    clientes.append(cliente)

    return "Cliente cadastrado com sucesso!"


def buscar_cliente(cpf: str):

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente

    return "Cliente não encontrado!"


def atualizar_telefone(cpf: str, novo_telefone: str):

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            cliente["telefone"] = novo_telefone
            return "Telefone atualizado com sucesso!"

    return "Cliente não encontrado!"


def deletar_cliente(cpf: str):

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            clientes.remove(cliente)
            return "Cliente deletado com sucesso!"

    return "Cliente não encontrado!"


def listar_clientes():

    if not clientes:
        return "Nenhum cliente cadastrado."

    return clientes
