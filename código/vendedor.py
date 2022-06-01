from threading import Thread, Lock, Event
import time, random
import nft



customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15
class Vendedor:


    def __init__(self, userName, risk_wanted, ad_status):
        self.userName= userName
        self.risk_wanted= risk_wanted
        self.ad_status=ad_status


	#aquí se definen las posibñes acciones que puede hacer nuestro baarbero
    AdEvent = Event()

	#el programa se pone en suspensión cunado no hay anuncios para enseñar
	def sleep(self):
		self.AdEvent.wait()

	#despertarse cuando hay anuncios que eneseñar
	def wakeUp(self):
		self.AdEvent.set()

	#la acción de mostrar el anuncio, cuando un cliente está viendo un anuncio, es un hilo que está siendo ejecutado
	def showAd(self, customer):
		#Set barber as busy
		self.AdEvent.clear()


		randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax+1)
		time.sleep(randomHairCuttingTime)
