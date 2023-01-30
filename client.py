import socket
import os
import time

class bcolors:
        RED   = "\033[1;31m"
        BLUE  = "\033[1;34m"
        CYAN  = "\033[1;36m"
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        BOLD    = "\033[;1m"
        REVERSE = "\033[;7m"

HOST = '127.0.1.1'
PORT = 5800

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    os.system("clear")

    try:
        client.connect((HOST, PORT))
        print(f'{bcolors.BOLD} 💹 Conectado com o servidor! {bcolors.RESET} \n')
    except:
        print(f'{bcolors.BOLD}{bcolors.RED}❌ Impossivel conectar com o servidor {HOST}:{PORT}')
        print(f'❗ Veja se a porta e o host estão correto! {bcolors.RESET}')
        time.sleep(2)
        exit()

    sendToServer(client)

def showServerResponse(client):
    while(True):
        message = client.recv(2048).decode('utf-8')

        if message != '':
            print(bcolors.BOLD + bcolors.BLUE + message + bcolors.RESET)
        else:
            print('Ocorreu algum erro durante o processo!!! \n Peço Desculpas pelo acontecido 😅')

        sendToServer(client)

def sendToServer(client):
    userChoose = userInterface()
    client.sendall(userChoose.encode())
    showServerResponse(client)

def cityMenu():
    os.system("clear")

    print(f"{bcolors.CYAN}💹 Escolha uma das cidade abaixo")
    time.sleep(1)

    print(f"""
[1] - Pirpirituba
[2] - Guarabira
[3] - João Pessoa
[4] - São Paulo
[5] - Rio de Janeiro
{bcolors.RESET} """)
    while True:
        try:
            option = int(input(f"{bcolors.BOLD}❇ Digite sua escolha: {bcolors.BOLD}"))
            if(option not in [1, 2, 3, 4, 5]):
                print("❌ Digite uma das opções acima")
            else:
                return option
            break
        except ValueError:
            print("\n ❌ Oops! Por favor digite somente números! 😠")

def userInterface():
    time.sleep(3)

    print(f"{bcolors.GREEN} {'='*20} Menu de opções {'='*20} {bcolors.RESET}")
    print(f"""{bcolors.CYAN}
💹 Escolha uma das opções abaixo
[1] - Cotação da bolsa de valores (USD, EUR, BTC)
[2] - Clima/Previsão do tempo
[3] - Mostrar catálogo de livros
[4] - Sair
{bcolors.RESET} """)

    while(True):
        try:
            time.sleep(1)
            option = int(input(f"{bcolors.BOLD}❇ Digite sua escolha: {bcolors.BOLD}"))

            if(option not in [1, 2, 3, 4]):
                print("❌ Digite uma das opções acima")
            if(option == 4):
                print("\n😄 Agradeço pelo uso!")
                time.sleep(1)
                exit()
            else:
                if(option == 1):
                    return f"{option}"
                if(option == 2):
                    city = cityMenu()
                    return f"{option}{city}"
                if(option == 3):
                    time.sleep(1.5)
                    return f"{option}"

        except ValueError:
            print("\n ❌ Oops! Por favor digite somente números! 😠")

        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    main()