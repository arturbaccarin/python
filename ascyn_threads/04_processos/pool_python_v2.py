import multiprocessing


def calcular(dado: int) -> int:
    return dado ** 2


def imprimir_nome_processo():
    print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')


def main():
    tamanho_pool = multiprocessing.cpu_count()*2

    print(f'Tamanho da pool: {tamanho_pool}.')

    # initializer: uma função que deve ser executada para cada processo criado
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close() # é igual o mp.start(). É a indicação que não tem nenhuma função a mais para mapear
    pool.join()

if __name__ == '__main__':
    main()