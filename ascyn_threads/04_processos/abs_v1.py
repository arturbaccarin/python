import threading
import time


def processar():
    print('[', end='', flush=True) # não vai esperar tudo para depois imprimir
    for _ in range(1, 11):
        print('#', end='', flush=True) # end: não vai pular linha
        time.sleep(1)
    print(']', end='', flush=True)


if __name__ == '__main__':
    ex = threading.Thread(target=processar)

    ex.start()
    ex.join()