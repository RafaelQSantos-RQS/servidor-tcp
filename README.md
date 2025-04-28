# 📡 Sistema Cliente-Servidor em Python

## Descrição
Projeto de comunicação em rede utilizando **Python** e o protocolo **TCP**.  
O sistema consiste em duas aplicações:
- **Servidor**: aguarda conexões de clientes e responde a mensagens enviadas.
- **Cliente**: envia mensagens ao servidor e exibe as respostas recebidas.

A comunicação é feita via **terminal/linha de comando**.

---

## Funcionamento
1. O **servidor** é iniciado e fica escutando conexões na porta `5400`.
2. O **cliente** se conecta ao servidor, solicita entrada do usuário e envia mensagens.
3. O **servidor** recebe a string enviada, processa, e envia uma resposta de volta.
4. A comunicação continua até o cliente digitar `"sair"`.

---

## Tecnologias Utilizadas
- Linguagem: **Python 3.x**
- Comunicação: **Sockets TCP**
- Gerenciamento de conexões simultâneas: **Threads**

---

## Como Executar

1. Abra dois terminais.
   
2. No primeiro terminal, execute o **servidor**:
   ```bash
   python TCPServer.py
   ```

3. No segundo terminal, execute o **cliente**:
   ```bash
   python TCPClient.py
   ```

4. No cliente, digite as mensagens desejadas.  
   Para encerrar, digite: `sair`.

---

## Observações
- O servidor aceita **múltiplas conexões simultâneas**.
- As mensagens são tratadas como **strings codificadas em UTF-8**.
- O projeto utiliza **apenas bibliotecas padrão** do Python.

---

## Protocolo Escolhido
> **TCP** (Transmission Control Protocol)

Justificativa:
- **Confiabilidade**: garante entrega correta dos pacotes.
- **Ordem**: mensagens chegam na sequência enviada.
- **Controle de conexão**: facilita o controle do fluxo de mensagens.

---

## Estrutura do Projeto
```
/ProjetoClienteServidor
│
├── TCPServer.py  # Código do servidor
└── TCPClient.py  # Código do cliente
```