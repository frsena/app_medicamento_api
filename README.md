# Minha API

objetivo deste aplicativo é cadastrar o medicamento para ter o controle da sua medicação.

---
## Como executar 

será necessario ter instalado na maquina o Python, recomenda-se a utilização da 3.12.3.


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
python -m venv env  
```

```
windows - env/Script/activate
```

```
(env)$ pip install -r requirements.txt
```

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Após a inicializacao do servidor, o arquivo db.sqlite3 será criado automaticamente com as duas tabelas do sistema.

Para carga inicial na tabela executar os seguintes passos:
    abrir um novo terminal e ir até a pasta do raiz do projeto.
    executar o comando no terminal - Python script_insert_banco

Certifique que a tabela remedio esteja devidamente populada no arquivo db.sqlite3

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar se a aplicacao esta no ar.


