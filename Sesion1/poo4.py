class Puerta():
    pass

class Salon():
    #Un salon que esta conformado de una puerta
    def __int__(self, puerta : Puerta):
        self.__puerta = puerta