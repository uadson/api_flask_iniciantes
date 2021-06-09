# api_flask_iniciantes
Tutorial para Iniciantes sobre como construir uma API em Python com o Micro Framework Flask

API - Application Programming Interface (Interface de Programação de Aplicações) é uma forma de integrar sistemas, são meios que fazem a conexão entre aplicações.

Abaixo segue um modelo simples de uma API CRUD, isto é, 

		C: create - cria um novo registro
		R: read - "ler" exibe as informações do registro
		U: update - atualiza dados do registro
		D: delete - apaga/exclui um registro

e que está disponível em : https://ichi.pro/pt/desenvolvimento-de-api-com-flask-para-iniciantes-178216365709514


Obs.: fundamental utilizar uma ferramente de teste como Postman, Katalon Studio, SoapUI, entre outras.

## LENDO/EXIBINDO VALORES - método GET

Ex.: a função get_buses retorna através da função jsonify(buses)
todos os elementos da lista como um objeto JSON


		@app.route('/buses')
		def get_buses():
			return jsonify(buses)

![get](https://user-images.githubusercontent.com/62815552/121402382-32091000-c930-11eb-9462-d244443740ef.png)


## LENDO/EXIBINDO VALORES DETERMINADOS - método GET

Na url deve ser informado o índice que corresponda ao item que será exibido
Ex.: /buses/0 -> exibirá o primeiro item da lista
bus recebe a item que será exibido através de buses[index] Ex.: get_bus(0) -> buses[0] -> bus = buses[0]


		@app.route('/buses/<int:index>')
		def get_bus(index):
			bus = buses[index]
			return jsonify(bus)

![get_one](https://user-images.githubusercontent.com/62815552/121403770-a2646100-c931-11eb-806e-06c5b5d223dd.png)


## ADICIONANDO DADOS - método POST

Os dados abaixo serão incluídos na lista buses:

"""	{

		"number_plate": "LXA 18",
		"manufacturer": "Honda",
		"model": "Honda H",
		"year": "2018",
		"capacity": 16
	}
"""
a variável bus receberá estes dados e será incluída à lista buses


		@app.route('/buses', methods=['POST'])
		def add_bus():
			bus = request.get_json()
			buses.append(bus)
			return bus


![post](https://user-images.githubusercontent.com/62815552/121404219-1ef73f80-c932-11eb-83d7-82c14838cbad.png)

## EXIBINDO OS DADOS - método GET

![getII](https://user-images.githubusercontent.com/62815552/121404801-b0ff4800-c932-11eb-81b0-bf24067df3cd.png)

## ATUALIZAR/UPDATE - método PUT

Na url deve ser informado um valor que corresponda ao índice de um elemento na lista
Ex.: /buses/1
A variável bus_to_update receberá os valores da lista
A função update_bus(index): receberá o valor do índice informado na url
Ex.: update_bus(1)
buses[index] recebe os dados atualizados.
a função jsonify exibe os dados como um objeto JSON


		@app.route('/buses/<int:index>', methods=['PUT'])
		def update_bus(index):
			bus_to_update = request.get_json()
			buses[index] = bus_to_update
			return jsonify(buses[index])

## ANTES

![get](https://user-images.githubusercontent.com/62815552/121402382-32091000-c930-11eb-9462-d244443740ef.png)

## EXECUTANDO O MÉTODO PUT

![put](https://user-images.githubusercontent.com/62815552/121406710-dab96e80-c934-11eb-927d-e3de9cd978c6.png)

## DEPOIS COM OS DADOS ATUALIZADOS

![getIII](https://user-images.githubusercontent.com/62815552/121406756-ed33a800-c934-11eb-908f-97d54a887836.png)

## EXCLUINDO DADOS - métod DELETE

Na url deve ser informado um valor que corresponda ao índice de um elemento na lista
Ex.: /buses/1
A função delete_bus(index): receberá o valor do índice informado na url
A variável deleted receberá a lista com o método pop e o índice do item que será excluído da lista


		@app.route('/buses/<int:index>', methods=['DELETE'])
		def delete_bus(index):
			deleted = buses.pop(index)
			return jsonify(deleted)