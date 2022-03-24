import socket
# faz a comunicação com o relacionamento da placa de rede com o SO
import sys
# sys: fornece acesso a variáveis e funções


def main():
    try:
        # AF_INET = IP
        # SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou.")
        print("Error: {}".format(e))
        sys.exit()

    print('Socket criado com sucesso')

    hostAlvo = input("Digite o Host ou Ip a ser conectado: ")
    portaAlvo = input("Digite a prota a ser conectada: ")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente TCP conectado com sucesso no Host: '+hostAlvo+' e na porta '+portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou.')
        print("Error: {}".format(e))
        sys.exit()


if __name__ == '__main__':
    main()

