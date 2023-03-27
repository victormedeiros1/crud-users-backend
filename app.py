import mysql.connector
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Conectando ao banco
connection = mysql.connector.connect(user='root', password='secret', host='localhost', port='3306', database='db_users')
cursor = connection.cursor()

# Instancionado o Flask e utilizando CORS
app = Flask('crud-users-backend') 
CORS(app)

@app.route('/')
def index():
    return users

@app.route('/user/<int:id>', methods=['GET'])
def getUser(id):
    cursor.execute(f"SELECT * FROM TB_USERS WHERE '{id}' = USE_ID;")
    userData = cursor.fetchall()

    # Verificando se algum usuário foi encontrado, se sim, retorna o ID
    if(len(userData) > 0):

        # Transformando em algo mais manuseável para o front [{}]
        keys = ('id', 'name', 'email', 'cpf', 'pis', 'password')

        result = []
        for data in userData:
            # Criando um novo dicionário para incluir os dados de endereço
            address = {}
            address['country'] = data[3]
            address['state'] = data[4]
            address['city'] = data[5]
            address['cep'] = data[6]
            address['street'] = data[7]
            address['number'] = data[8]
            address['complement'] = data[9]

            # Criando o dicionário principal do usuário sem os dados de endereço
            user = dict(zip(keys, [data[0], data[1], data[2], data[10], data[11], data[12]]))
            user['address'] = address

            result.append(user)

        objectWithData = json.dumps(result)

        return objectWithData
    else:
        return {'status': 404}

@app.route('/auth', methods=['POST'])
def auth():
    # Pegando os dados do usuário
    formData = request.get_json()
    login = formData['login']
    password = formData['password']
    
    # Fazendo a busca no banco
    cursor.execute(f"SELECT USE_ID, USE_NAME FROM TB_USERS WHERE (USE_EMAIL = '{login}' OR USE_CPF = '{login}' OR USE_PIS = '{login}') AND USE_PASSWORD = '{password}';")
    userData = cursor.fetchall()

    # Verificando algum usuário foi encontrado, sesim retorna o ID
    if(len(userData) > 0):

        # Transformando em algo mais manuseável para o front [{}]
        keys = ('id', 'name' )

        result = []
        for data in userData:
            result.append(dict(zip(keys, data)))

        objectWithData = json.dumps(result)

        return objectWithData
    else:
        return {'status': 404}

@app.route('/create-user', methods=['POST'])
def createUser():
    formData = request.get_json()
    name = formData['name']
    email = formData['email']
    country = formData['address']['country']
    state = formData['address']['state']
    city = formData['address']['city']
    cep = formData['address']['cep']
    street = formData['address']['street']
    number = formData['address']['number']
    complement = formData['address']['complement']
    cpf = formData['cpf']
    pis = formData['pis']
    password = formData['password']

    cursor.execute(
        f"INSERT INTO TB_USERS(USE_NAME, USE_EMAIL, USE_COUNTRY, USE_STATE, USE_CITY, USE_CEP, USE_STREET, USE_NUMBER, USE_COMPLEMENT, USE_CPF, USE_PIS, USE_PASSWORD) VALUES('{name}', '{email}', '{country}', '{state}', '{city}', '{cep}', '{street}', '{number}', '{complement}', '{pis}', '{cpf}', '{password}')")
    connection.commit()
    
    return 'REQUISIÇÃO BEM SUCEDIDA'
app.run(port = 5000, host='localhost', debug=True)