from Subclase1.coche import*

class Camion(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
        
    def __str__(self):
        return Coche.__str__(self) + ", {} Kg".format(self.carga)

c1 = Camion("Verde", 4, 150, 1200,3000)
