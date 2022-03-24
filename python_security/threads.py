from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print('Carro: ', piloto, trajeto)
        trajeto += velocidade
        time.sleep(0.5)



t_carro1 = Thread(target=carro, args=[1, '1'])
t_carro2 = Thread(target=carro, args=[2, '2'])

t_carro1.start()
t_carro2.start()