
from postgrest.exceptions import APIError
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
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

class Cliente(BaseModel):
    nome: str
    cpf: str
    telefone: str

@app.post("/clientes")
def cadastrar_cliente_banco(cliente: Cliente):
    try:
        resposta = (
        supabase
        .table("clientes")
        .insert(cliente.model_dump())
        .execute()
    )
    except APIError as erro:
        if erro.code == "23505":
            raise HTTPException(status_code=409, detail="CPF já cadastrado")
        raise    
    return resposta.data

@app.get("/clientes")
def listar_clientes_banco():
    resposta = (
    supabase
    .table("clientes")
    .select("*")
    .execute()
)

    return resposta.data


@app.get("/clientes/{cpf}")
def buscar_cliente_api(cpf: str):
    resposta = (
        supabase
        .table("clientes")
        .select("*")
        .eq("cpf", cpf)
        .execute()
    )

    if not resposta.data:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return resposta.data[0]


@app.patch("/clientes/{cpf}")
def atualizar_telefone_api(cpf: str, novo_telefone: str):
    resposta = (
        supabase
        .table("clientes")
        .update({"telefone": novo_telefone})
        .eq("cpf", cpf)
        .execute()
    )

    if not resposta.data:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return {"message": "Telefone atualizado com sucesso!"}


@app.delete("/clientes/{cpf}")
def deletar_cliente_api(cpf: str):
    resposta = (
        supabase
        .table("clientes")
        .delete()
        .eq("cpf", cpf)
        .execute()
    )

    if not resposta.data:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return {"message": "Cliente deletado com sucesso!"}


class Veiculo(BaseModel):
    placa: str
    renavam: str
    chassi: str

@app.post("/clientes/{cpf}/veiculos")
def cadastrar_veiculo(cpf: str, veiculo: Veiculo):
    resposta_cliente = (
        supabase
        .table("clientes")
        .select("*")
        .eq("cpf", cpf)
        .execute()
    )

    if not resposta_cliente.data:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    veiculo_data = veiculo.model_dump()
    veiculo_data["cliente_id"] = resposta_cliente.data[0]["id"]


    try:
        resposta_veiculo = (
            supabase
            .table("veiculos")
            .insert(veiculo_data)
            .execute()
        )

    except APIError as erro:
        if erro.code == "23505":
            raise HTTPException(status_code=409, detail="Placa, RENAVAM ou chassi já cadastrado")
        raise

    return {"message": "Veículo cadastrado com sucesso!"}

@app.get("/clientes/{cpf}/veiculos")
def listar_veiculos(cpf: str):
    resposta_cliente = (
        supabase
        .table("clientes")
        .select("*")
        .eq("cpf", cpf)
        .execute()
    )

    if not resposta_cliente.data:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    cliente_id = resposta_cliente.data[0]["id"]

    resposta_veiculos = (
        supabase
        .table("veiculos")
        .select("*")
        .eq("cliente_id", cliente_id)
        .execute()
    )

    return resposta_veiculos.data

