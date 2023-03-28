![thumbnail](https://user-images.githubusercontent.com/66215200/228317746-b574f656-aa0a-4430-9138-fe64555de2cb.jpg)

# crud-users-backend

Esse é o backend da aplicação, ele inclui a API feita em Python com Flask e a criação do container usando Docker e MySQL.

Montei um pequeno guia para a criação dessa aplicação com metas, conceitos e tecnologias para estudar, para acessá-lo clique [aqui](https://www.notion.so/Desafio-PontoTel-Guia-autoral-cc84efa4f297441d9ab4c6745ecef69f?pvs=4).

Algumas dependências devem ser instaladas, são elas:

- flask
- flask_jwt_extended
- flask_cors
- mysql-connector-python

Ex: `pip install flask`

### Passo a passo de como rodar o backend. Vamos lá, na pasta do projeto:

1º Criação do container Docker que comporta o banco dados.

```docker-compose -up -d```

Ao executar esse comando, um container Docker com a imagem do MySQL será criado e um arquivo `init.sql` contendo a única tabela necessária para a aplicação será construída.

2º Levantando o servidor da API.

`python app.py`

Esse comando irá rodar um servidor local na `porta 5000`.

## Testando sua API

Acesse: http://localhost:5000/ uma mensagem deverá aparecer!
