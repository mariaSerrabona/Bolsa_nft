#fichero main donde solo se ejecutara el código
#para ello, será necesario llamar a las demás clases del proyecto


import time, random

import comprador
import nft
import vendedor


#Interval in seconds

#se define en segundos las diferentes duraciones de los procesos
customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15


#se ejecutan los hilos para cada persona, cada persona es un hilo
if '_name_' == '_main_':

	customers = []
	customers.append(comprador.Comprador('María'))
	customers.append(comprador.Comprador('Rubén'))
	customers.append(comprador.Comprador('Alex'))
	customers.append(comprador.Comprador('Pablo'))
	customers.append(comprador.Comprador('Andrea'))
	customers.append(comprador.Comprador('Sofía'))
	customers.append(comprador.Comprador('Mónica'))
	customers.append(comprador.Comprador('Olga'))
	customers.append(comprador.Comprador('Fernando'))
	customers.append(comprador.Comprador('Pepa'))
	customers.append(comprador.Comprador('Roberto'))
	customers.append(comprador.Comprador('Joaquín'))
	customers.append(comprador.Comprador('Martina'))
	customers.append(comprador.Comprador('Mencia'))
	customers.append(comprador.Comprador('Tomas'))
	customers.append(comprador.Comprador('Cristina'))
	customers.append(comprador.Comprador('Pedro'))

	barber = vendedor.Vendedor()

	nft = nft.nft(barber, numberOfSeats=3)
	nft.openShop()

	while len(customers) > 0:
		c = customers.pop()
		#New customer enters the barbershop
		nft.enterBarberShop(c)
		customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1)
		time.sleep(customerInterval)