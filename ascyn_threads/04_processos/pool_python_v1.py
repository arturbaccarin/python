import multiprocessing


def calcular(dado: int) -> int:
    return dado ** 2


def main():
    tamanho_pool = multiprocessing.cpu_count()*2

    print(f'Tamanho da pool: {tamanho_pool}.')

    # processes: a quantidade de processos que serão criados
    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close() # é igual o mp.start(). É a indicação que não tem nenhuma função a mais para mapear
    pool.join()


if __name__ == '__main__':
    main()