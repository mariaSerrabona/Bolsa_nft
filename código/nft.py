class nft:

    tipo_riesgo=['alto', 'bajo', 'medio']
    name='1'
    precio=8402.38
    descripcion='nft bonito'
    vendedor='userA'

    def __init__(self,tipo_riesgo, name, precio, descripcion, vendedor):
        self.tipo_riesgo=tipo_riesgo
        self.name=name
        self.precio=precio
        self.descripcion=descripcion
        self.tipo_riesgo=vendedor

    #se revuelve toda la información de un nft
    def info_nft(self):

        print('NFT con un riesgo: '+self.tipo_riesgo)
        print('Nombre del NFT: '+self.name)
        print('precio del NFT: '+self. precio)
        print('Detalles del NFT: '+self.descripcion)