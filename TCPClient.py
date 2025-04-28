# Protocolo utilizado: TCP

import socket


# Função principal do cliente
def start_client():
    server_address = '127.0.0.1'  # Endereço do servidor (localhost)
    server_port = 5400  # Porta do servidor

    # Criação do socket TCP e conexão com o servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_address, server_port))
        print("[INFO] Conectado ao servidor.")

        while True:
            # Solicita ao usuário uma mensagem para enviar
            message = input("Digite uma mensagem (ou 'sair' para encerrar): ")

            if message.lower() == 'sair':
                print("[INFO] Encerrando conexão com o servidor.")
                break  # Sai do loop e fecha a conexão

            # Envia a mensagem para o servidor
            client_socket.send(message.encode())

            # Aguarda a resposta do servidor
            data = client_socket.recv(1024).decode()
            print(f"Resposta do servidor: {data}")


# Início da execução do cliente
if __name__ == "__main__":
    start_client()
