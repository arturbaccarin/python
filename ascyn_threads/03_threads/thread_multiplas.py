import threading # Passo 1
import time

# O SO tem um algoritmo de escalonamento que vai decidir
# quando e por quanto tempo determinada thread será executada
# no processador 

def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)

def main():
    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('buraco', 8)),
        threading.Thread(target=contar, args=('dinheiro', 23)),
        threading.Thread(target=contar, args=('pato', 12)),
    ] # Passo 2

    [th.start() for th in threads] # adiciona a nossa thread na pool de threads prontas para a execução. ELE NÃO EXECUTA!!! # Passo 3

    print('Podemos fazer outras coisas enquanto a thread vai executando!')
    print('Olá ' * 5)

    for i in range(20):
        time.sleep(0.3)
        print(i)
    
    [th.join() for th in threads] # avisa para ficar aguardando aqui até a threads terminar a execução # Passo 4

    print('Pronto!')



if __name__ == '__main__':
    main()


