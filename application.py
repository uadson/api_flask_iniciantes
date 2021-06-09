"""Construção de uma API CRUD para gerenciar barramentos de 
motores AA. 
Disponível em: https://ichi.pro/pt/desenvolvimento-de-api-com-flask-para-iniciantes-178216365709514

Obs.: fundamental utilizar uma ferramente de teste como Postman
As informações necessárias para coleta serão:

	Number Plate
	Manufacturer
	Model
	Year
	Capacity"""


# 1. Imports
from flask import Flask, jsonify, request


# Definindo o app que será uma instância de Flask
app = Flask(__name__)


# Lista com os dados:

buses = [

	{

		"number_plate": "NAX 123",
		"manufacturer": "Toyota",
		"model": "Hiace",
		"year": "2009",
		"capacity": 18
	},
	{

		"number_plate": "LX Z19",
		"manufacturer": "Ford",
		"model": "FordX",
		"year": "2010",
		"capacity": 45
	}
]

# LENDO/EXIBINDO VALORES - método GET
# Ex.: a função get_buses retorna através da função jsonify(buses)
# todos os elementos da lista como um objeto JSON
@app.route('/buses')
def get_buses():
	return jsonify(buses)

#GET um determinado item
# Na url deve ser informado o índice que corresponda ao item que será exibido
# Ex.: /buses/0 -> exibirá o primeiro item da lista
# bus recebe a item que será exibido através de buses[index] Ex.: get_bus(0) -> buses[0] -> bus = buses[0]
@app.route('/buses/<int:index>')
def get_bus(index):
	bus = buses[index]
	return jsonify(bus)

# ADICIONANDO DADOS - método POST
# Os dados abaixo serão incluídos na lista buses:

"""	{

		"number_plate": "LXA 18",
		"manufacturer": "Honda",
		"model": "Honda H",
		"year": "2018",
		"capacity": 16
	}
"""
# a variável bus receberá estes dados e será incluída à lista buses
@app.route('/buses', methods=['POST'])
def add_bus():
	bus = request.get_json()
	buses.append(bus)
	return bus

# UPDATE - método PUT
# Na url deve ser informado um valor que corresponda ao índice de um elemento na lista
# Ex.: /buses/1
# A variável bus_to_update receberá os valores da lista
# A função update_bus(index): receberá o valor do índice informado na url
# Ex.: update_bus(1)
# buses[index] recebe os dados atualizados.
# a função jsonify exibe os dados como um objeto JSON
@app.route('/buses/<int:index>', methods=['PUT'])
def update_bus(index):
	bus_to_update = request.get_json()
	buses[index] = bus_to_update
	return jsonify(buses[index])

# EXCLUINDO DADOS - métod DELETE
# Na url deve ser informado um valor que corresponda ao índice de um elemento na lista
# Ex.: /buses/1
# A função delete_bus(index): receberá o valor do índice informado na url
# A variável deleted receberá a lista com o método pop e o índice do item que será excluído da lista
@app.route('/buses/<int:index>', methods=['DELETE'])
def delete_bus(index):
	deleted = buses.pop(index)
	return jsonify(deleted)

if __name__ == '__main__':
	app.run(debug=True)