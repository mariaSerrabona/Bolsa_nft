
#UN INTENTO DE HACER LOS HILOS DEL BARBERO.
#ME DA ERROR DE IDENTACIÓN Y POR ESO NO LO PUEDO PROBAR



#clase que representa a la barbería
#se importan hilo para poder representar a los usuarios.

from threading import Thread, Lock, Event
import time, random
import vendedor
import comprador

#este mutex funciona como un bloqueador del hilo
#eso significa que se bloqueará la ejecución el siguiente hilo cuando otro esté en proceso
#en la vida real significaría, no dejar pasar a un cliente mientras ya se está atendiendo a uno
mutex = Lock()

#Interval in seconds
#del mismo modo, se definen los intervalos en segundos para diferentes pprocesos.
customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15


class nft:
    waitingCustomers = []

#constructor con todos los atributos que definen a una barbería
	def _init_(self, nft, numberOfAds):
		self.nft = nft
		self.numberOfAds = numberOfAds

#señal de que el mercado de compras de nfts está abierto: se pueden empezar a ejecutar los hilos en orden
	def openShop(self):
		workingThread = Thread(target = self.barberGoToWork)
		workingThread.start()

	#mientras no haya un bloqueo, se enseñan los anuncios
	def barberGoToWork(self):
		while True:
			mutex.acquire()
			#sentencias para poder pasar de un anuncio a otro, los anuncios se almacenan en la lista de espera
			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]
				del self.waitingCustomers[0]
				mutex.release()
				self.vendedor.showAd(c)
			else:
				#Si no hay anuncios en espera, el programana no hacenada y no enseña anuncios
				mutex.release()
				vendedor.sleep()

#generar la cola para mostrar los anuncios
	def enterBarberShop(self, customer):
		mutex.acquire()

		if len(self.waitingCustomers) == self.numberOfAds:
			mutex.release()
		else:
			self.waitingCustomers.append(c)
			mutex.release()
			vendedor.Vendedor.wakeUp()