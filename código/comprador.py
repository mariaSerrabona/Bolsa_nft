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

            print(f"El consumidor- {userName} Ha visto el anuncio {count+1}")

            count+=1

            q.task_done() # Envía una señal después de comer

            time.sleep(1)


    #función para cuando un nft le interesa al comprador
    def interesa_nft(userName):
        print('Hola! Soy '+userName+ ' me ha interesado tu anuncio y quiero comprar tu nft')
        #no sé cómo notoficar el vendedor