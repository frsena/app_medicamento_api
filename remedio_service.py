
from flask_openapi3 import Tag

from model import Session, Remedio
from logger import logger
from app import app
from schemas import *

remedio_tag = Tag(name="Remedio", description="Listar todos os remedios")


@app.get('/remedios', tags=[remedio_tag],
         responses={"200": ListagemRemedioSchema, "404": ErrorSchema})
def busca_remedios():
    """ Retorna todos os remedios cadastrados
    """
    session = Session()
    remedios = session.query(Remedio).all()

    if not remedios:
        # se não há produtos cadastrados
        return [], 200
    else:
        logger.debug(f"%d produtos econtrados" % len(remedios))
        return remedios_view(remedios), 200
