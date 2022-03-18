from typing import Generator


def fibo() -> Generator[int, None, None]:
    valor: int = 0
    proximo: int = 1

    while True:
        valor, proximo = proximo, valor + proximo
        yield valor # devolve o valor e espera a próxima chamada

if __name__ == '__main__':
    for n in fibo():
        print(n, end=', ')
        if n > 100:
            break

    print('\nPronto!')

# generator é um tipo de co-rotina que pode ser controlada a execução