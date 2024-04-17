from pydantic import BaseModel
from typing import List, Optional
from model import Remedio


class RemedioSchema(BaseModel):
    """ Define como o remedio deve ser representado
    """
    id: int = 1
    nome: str = "Nesoldina"

class ListagemRemedioSchema(BaseModel):
    """ Define como uma listagem de medicamento será retornada.
    """
    remedios:List[RemedioSchema]   


def remedio_view(remedio: Remedio):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return RemedioSchema (
        id = remedio.id,
        nome = remedio.nome).model_dump()


def remedios_view(remedios: Remedio):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    resultado = []
    for remedio in remedios:
       # resultado.append({
       #     "id": remedio.id,
        #    "nome": remedio.nome
        #})
        resultado.append(RemedioSchema (
                    id = remedio.id,
                    nome = remedio.nome).model_dump())
    return resultado