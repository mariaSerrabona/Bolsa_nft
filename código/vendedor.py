from threading import Thread, Lock, Event
import time, random
import nft



customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15
class Vendedor:

    userName='hola'
    risk_wanted='low'
    ad_status='accepted'


    def __init__(self, userName, risk_wanted, ad_status):
        self.userName= userName
        self.risk_wanted= risk_wanted
        self.ad_status=ad_status


	#aquí se definen las posibñes acciones que puede hacer nuestro baarbero
    barberWorkingEvent = Event()

	#dormi cuando no se tienen clientes en la cola
	def sleep(self):
		self.barberWorkingEvent.wait()

	#despertarse cuando hay trabajo por hacer
	def wakeUp(self):
		self.barberWorkingEvent.set()

	#la acción de cortar el pelo, bloqueando el hilo de ejecución del cliente que está siendo atendido
	def cutHair(self, customer):
		#Set barber as busy
		self.barberWorkingEvent.clear()

		print ('{0} is having a haircut'.format(customer.name))

		randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax+1)
		time.sleep(randomHairCuttingTime)
		print ('{0} is done'.format(customer.name))
