
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
	def _init_(self, barber, numberOfSeats):
		self.barber = barber
		self.numberOfSeats = numberOfSeats

#señal de que la barbería está abierta: se pueden empezar a ejecutar los hilos en orden
	def openShop(self):
		print ('Barber shop is opening')
		workingThread = Thread(target = self.barberGoToWork)
		workingThread.start()

	#mientras no haya un bloqueo, el barbero se pone a trabajar
	def barberGoToWork(self):
		while True:
			mutex.acquire()
			#sentencias para poder pasar de un cliente a otro, clientes que se almacenan en la lista de espera
			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]
				del self.waitingCustomers[0]
				mutex.release()
				self.vendedor.cutHair(c)
			else:
				#mientras no haya clientes en espera, el barbero se va a dormir
				mutex.release()
				print('Aaah, all done, going to sleep')
				vendedor.sleep()
				print('Barber woke up')

#generar la cola para atender a los clientes
	def enterBarberShop(self, customer):
		mutex.acquire()
		print ('>> {0} entered the shop and is looking for a seat'.format(comprador.name))

		if len(self.waitingCustomers) == self.numberOfSeats:
			print ('Waiting room is full, {0} is leaving.'.format(comprador.name))
			mutex.release()
		else:
			print ('{0} sat down in the waiting room'.format(customer.name))
			self.waitingCustomers.append(c)
			mutex.release()
			vendedor.Barber.wakeUp()