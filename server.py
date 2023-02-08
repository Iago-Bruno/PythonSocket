import socket
import threading
import requests
import json
import time
import os

HOST = '127.0.1.1'
PORT = 5800
LISTENER_LIMIT = 5

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        os.system("clear")
        print(f'Servidor {HOST}:{PORT} online')
    except:
        print(f'Impossivel se conectar com o host {HOST} e porta {PORT}')

    server.listen(LISTENER_LIMIT)

    while True:
        try:
            client, address = server.accept()
            print(f'Cliente {address[0]}:{address[1]} conectado com sucesso\n')

            threading.Thread(target=getUserResponse, args=(client, )).start()
        except:
            print("\nAté a proxima meu caro 🤙👋")
            time.sleep(1)
            exit()

def sendMensage(client, mensagem):
    client.sendall(mensagem.encode())

def getUserResponse(client):
    while True:
        choosenOption = client.recv(2048).decode('utf-8')
        try:
            if(int(choosenOption) == 1):
                response = getStockExchange()
            if(int(choosenOption[0]) == 2):
                response = getWeather(choosenOption[1])
            if(int(choosenOption) == 3):
                response = getBooksData()
            sendMensage(client, response)
        except:
            print("❌ Usuário cancelou o uso da aplicação ou escreveu algum comando errado ❗ \n")
            return ''

def getStockExchange():
    data = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = data.json()

    cotacaoDolar = cotacao['USDBRL']['bid']
    cotacaoEuro = cotacao['EURBRL']['bid']
    cotacaoBTC = cotacao['BTCBRL']['bid']

    text = f"""
Dolar: {cotacaoDolar}
Euro: {cotacaoEuro}
BitCoin: {cotacaoBTC}
    """

    return text

def getWeather(option):
    citys = ['pirpirituba', 'guarabira', 'joão pessoa', 'são paulo', 'rio de janeiro']

    API_KEY = "1affdc15b5cb4e960e5a73bda450eec9"
    cidade = citys[int(option)-1]
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    req = requests.get(link)
    req_json = req.json()

    descricao = req_json['weather'][0]['description']
    thermal = int(req_json['main']['feels_like'] - 273.15)
    temperatura = int(req_json['main']['temp'] - 273.15)

    text = f"""
Temperatura: {temperatura}°
Sensação térmica: {thermal}°
Céu: {descricao}
    """
    return text

def getBooksData():
    count = 0
    text = ""

    with open("catalogo.json") as file:
        data = json.load(file)

    for item in data['books']:
        count += 1
        text += f"\n{'='*30} Livro {count} {'='*30} \n"

        for chave, valor in item.items():
            text += f"{chave}: {valor} \n"

    return text

if __name__ == '__main__':
    main()