# Protocolo utilizado: TCP

import socket
import threading


# Classe que representa uma thread para lidar com cada cliente conectado
class ClientThread(threading.Thread):
    def __init__(self, client_socket, address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address
        print(f"[INFO] Conectado a {address}")

    def run(self):
        try:
            while True:
                # Recebe a mensagem enviada pelo cliente
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break  # Cliente desconectou
                print(f"Recebido de {self.address}: {data}")

                # Processa a mensagem: transforma em maiúsculas
                processed_data = data.upper()
                print(f"Servidor processou: {data} -> {processed_data}")

                # Envia a resposta de volta ao cliente
                self.client_socket.send(processed_data.encode())
        except Exception as e:
            print(f"[ERRO] {e}")
        finally:
            self.client_socket.close()
            print(f"[INFO] Conexão com {self.address} encerrada.")


# Função principal do servidor
def start_server():
    server_port = 5400
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', server_port))
    server_socket.listen()

    print(f"[INFO] Servidor TCP escutando na porta {server_port}...")

    while True:
        # Aceita novas conexões
        client_socket, addr = server_socket.accept()
        # Cria uma nova thread para cada cliente conectado
        thread = ClientThread(client_socket, addr)
        thread.start()


# Início da execução do servidor
if __name__ == "__main__":
    start_server()
