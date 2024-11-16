from datetime import datetime
from typing import Optional, Literal, List

from fastapi import FastAPI
from pydantic import BaseModel, constr


app = FastAPI()


# Entity Cliente
class Cliente(BaseModel):
    id: Optional[int] = None
    nome: constr(max_length=20)
    tipo_atendimento: Literal['N', 'P']
    data: datetime
    status_atendimento: bool


# Request
class ClienteRequest(BaseModel):
    nome: constr(max_length=20)
    tipo_atendimento: Literal['N', 'P']


# Response
class ClienteResponse:
    posicao: int
    nome: str
    data_chegada: datetime

    def __init__(self, posicao: int, nome: str, data_chegada: datetime):
        self.posicao = posicao
        self.nome = nome
        self.data_chegada = data_chegada


# Seed de dados
db_clientes: List[Cliente] = [
    Cliente(id=1, nome="Maria", tipo_atendimento='P', data=datetime.now(), status_atendimento=False),
    Cliente(id=2, nome="João", tipo_atendimento='N', data=datetime.now(), status_atendimento=False),
    Cliente(id=3, nome="John Doe", tipo_atendimento='N', data=datetime.now(), status_atendimento=False),
]


@app.get("/fila")
def get_all():
    resposta: List[ClienteResponse] = []
    if len(db_clientes) == 0:
        return {"info": db_clientes, "status": 200}
    for cliente in db_clientes:
        if cliente.status_atendimento == False:
            resposta.append(ClienteResponse(posicao=cliente.id, nome=cliente.nome, data_chegada=cliente.data))
    return {"info": resposta, "status": 200}


@app.get("/fila/{id}")
def get_by_id(id: int):
    for cliente in db_clientes:
        if cliente.id == id:
            return {
                "info": ClienteResponse(posicao=cliente.id, nome=cliente.nome, data_chegada=cliente.data),
                "status": 200
            }
    return {"mensagem": "Cliente não localizado.", "status": 404}


@app.post("/fila")
def create(cliente: ClienteRequest):
    novo_cliente = Cliente(
        nome=cliente.nome,
        tipo_atendimento=cliente.tipo_atendimento,
        data=datetime.now(),
        status_atendimento=False
    )
    novo_cliente.id = db_clientes[-1].id + 1
    db_clientes.append(novo_cliente)
    return {"mensagem": "Cliente adicionado na fila.", "status": 201}
