from abc import ABC

class Vehiculo(ABC, object):
    def arrancar(self):
        print("Arrancar vehiculo")

class Auto(Vehiculo):
    pass

miCarro = Auto()
miCarro.arrancar() 