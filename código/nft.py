import threading

#lo primero que vamos a hacer es crear un nft como un hilo básico

class hilo:
    def __intit__(self, name, risk):
        self.name=name
        self.risk=risk


#creamos una función cualquiera para ver que funciona
hilos=[]
def creating(hilo_apertura):
    name1=input('nombre: ')
    risk1=input('riesgo: ')

    t=threading.Thread(target=creating, args=[name1, risk1])
    t.start()
    hilos.append(t)

def closing (hilo_cierre):
    hilo_cierre.join()


hilo1=hilo('hilouno', 'low')
creating(hilo1)

for hilo in hilos:
    closing(hilo)


print('hilos termiandos')