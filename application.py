"""Construção de uma API CRUD para gerenciar barramentos de 
motores AA. 
Disponível em: https://ichi.pro/pt/desenvolvimento-de-api-com-flask-para-iniciantes-178216365709514

As informações necessárias para coleta serão:

	Number Plate
	Manufacturer
	Model
	Year
	Capacity"""


# 1. Imports
from flask import Flask, jsonify, 


# Definindo o app que será uma instância de Flask
app = Flask(__name__)


# Lista com os dados:

buses = [

	{

		'number_plate': 'NAX 123',
		'manufacturer': 'Toyota',
		'model': 'Hiace',
		'year': '2009',
		'capacity': 18
	},
	{

		'number_plate': 'LX Z19',
		'manufacturer': 'Ford',
		'model': 'FordX',
		'year': '2010',
		'capacity': 45
	}
]

# Definindo uma rota para função que fará a coleta de todos os dados
@app.route('/buses')
def get_buses():
	return jsonify(buses)
	

if __name__ == '__main__':
	app.run(debug=True)