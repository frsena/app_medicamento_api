from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS


info = Info(title="Controle de Medicamento", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)


import medicamento_service
import documentacao_service 
import remedio_service 

app.run()