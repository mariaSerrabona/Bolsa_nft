import threading
import time

#lo primero que vamos a hacer es crear un nft como un hilo básico

#creamos una función cualquiera para ver que funciona
def creating(name, type_risk):
    print('nft name is: '+ name)
    time.sleep(2)
    print('nft risk type is: '+type_risk)

hilos=[]

for _ in range (3):
    name=input('nombre: ')
    risk=input('riesgo: ')

    t=threading.Thread(target=creating, args=[name, risk])
    t.start()
    hilos.append(t)

for hilo in hilos:
    hilo.join()

print('hilos termiandos')