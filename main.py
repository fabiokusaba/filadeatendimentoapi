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


# Seed de dados
db_clientes: List[Cliente] = [
    Cliente(id=1, nome="Maria", tipo_atendimento='P', data=datetime.now(), status_atendimento=False),
    Cliente(id=2, nome="João", tipo_atendimento='N', data=datetime.now(), status_atendimento=False),
    Cliente(id=3, nome="John Doe", tipo_atendimento='N', data=datetime.now(), status_atendimento=False),
]


@app.get("/fila")
def get_all():
    resposta = []
    if len(db_clientes) == 0:
        return {"data": db_clientes, "status": 200}
    for cliente in db_clientes:
        if cliente.status_atendimento == False:
            resposta.append({"posicao": cliente.id, "nome": cliente.nome, "data_chegada": cliente.data})
    return {"data": resposta, "status": 200}
