from abc import ABC

class Vehiculo(ABC, object):
    def arrancar(self):
        print("Arrancar vehiculo")

#Corresponde al principio SOLID O
#(Open/Closed)
class Auto(Vehiculo):
    def __int__(self):
        super().__int__()
        print("Constructor auto")

    def arrancar(self):
        print("Arrancar auto")

class Moto(Vehiculo):
    def __int__(self):
        super().__int__()
        print("Constructor moto")

    def arrancar(self):
        print("Arrancar moto")

miCarro = Auto()
#miCarro.arrancar()
miMoto = Moto()
#miMoto.arrancar()

listadoVehiculos = [miCarro]
listadoVehiculos.append(miMoto)

for vehiculo in listadoVehiculos:
    vehiculo.arrancar()