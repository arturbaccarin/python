import threading # Passo 1
import time

def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)

def main():
    th = threading.Thread(target=contar, args=('elefante', 10)) # Passo 2

    th.start() # adiciona a nossa thread na pool de threads prontas para a execução. ELE NÃO EXECUTA!!! # Passo 3

    print('Podemos fazer outras coisas enquanto a thread vai executando!')
    print('Olá ' * 5)

    for i in range(20):
        time.sleep(0.3)
        print(i)
    
    th.join() # avisa para ficar aguardando aqui até a threads terminar a execução # Passo 4

    print('Pronto!')


if __name__ == '__main__':
    main()