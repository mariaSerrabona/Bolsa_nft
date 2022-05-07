from queue import Queue

from threading import Thread

import time


class Comprador:

    userName='hola'
    risk_wanted='low'
    ad_status='accepted'


    def __init__(self, userName, risk_wanted, ad_status):
        self.userName= userName
        self.risk_wanted= risk_wanted
        self.ad_status=ad_status

    def informacion(self):
        print('Nombre del comprador: '+str(self.userName))
        print('Riesgo requerido por el comprador : '+str(self.risk_wanted))
        print('Estado del anuncio: '+str(self.ad_status))

    #consumidor de anuncios, de nfts

    def customer(userName, numero):
        q = Queue(10)
        count = 0

        while (count<numero):

            print(f"El consumidor- {userName} está comiendo el bollo {count+1}")

            count+=1

            q.task_done() # Envía una señal después de comer

            time.sleep(1)


class Vendedor:
    userName='hola'

    def __init__(self, userName):
        self.userName=userName

    def informacion(self):
        print('Nombre del vendedor: '+str(self.userName))


    #productor de anuncios de nft
    def producer(userName,numero):
        q = Queue(10)
        """Productor"""

        count = 0 #mostrador

        while (count<numero):

            q.join()

            q.put(count)

            print(f"{userName} esta produciendo el anuncio {count+1}")

            count+=1


#ver los NFTs, como si fueran bollos que uno los produce (vendedor) y otro los consume (comprador)



if __name__ == '__main__':

    numero=input('Introduce el número de bollos que se quiere realizar: ')
    numero=int(numero)

    t1 = Thread(target=Vendedor.producer,args=(Vendedor.userName,numero))

    t2 = Thread(target=Comprador.customer,args=(Comprador.userName,numero))

    t1.start()

    t2.start()
