
import threading

#la base de los hilos es generarlos primero, y generar una función con cada una de las opciones que el hilo puede realizar.

#en este caso, un NFT puede relizar la opción de ser rechazado, entonces se cierra el hilo y no se vuelve a mostrar
                            #o bien puede ser aceptado entonces se tendrá que enviar un mensaje al vendedor notificando la venta



class nft(threading.Thread):

    semaforo=threading.Lock() #determina el bloqueo del hilo para que dos hilos no se puedan superponer
    estado=[]   #se conoce el estado de cada hilo, si el nft se quiere comrpar o descartar

    #constructor de la clase nft
    def __init__(self, name, tipo_riesgo, precio, descripcion):
        self.name=name
        self.tipo_riesgo=tipo_riesgo
        self.precio=precio
        self.descripcion=descripcion

    def descartar(self): #función que se ejecutará cuando un nft sea descartado por el comprador
        nft.estado[self.name] = 'siguiente'
        nft.semaforo.release() #se deja el nft

    def comprar(self):  #función que se ejecutará cuando un nft se quiera comprar
        nft.estado[self.name] = 'comprar'
        print('se ha comprado el nft: '+self.name)




if __name__=="__main__":
    N=input('Numero de anuncios que se quiere: ')
    N=int(N)

    name=input('nombre: ')
    tipo_riesgo=input('tipo_riesgo: ')
    precio=input('precio: ')
    descripcion=input('descripcion: ')
    lista=[]
    for i in range(N):
        lista.append(nft(name, tipo_riesgo, precio, descripcion)) #AGREGA UN FILOSOFO A LA LISTA

    for f in lista:
        f.start() #ES EQUIVALENTE A RUN()

    for f in lista:
        f.join() #BLOQUEA HASTA QUE TERMINA EL THREAD
