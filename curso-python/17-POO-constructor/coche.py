class Coche:
    Color = "negro"
    Velocidad = 300
    Marca = "ferrare"

    def __init__(self, color, velocidad, marca ):
        self.Color = color
        self.Velocidad = velocidad
        self.Marca = marca


    def setVelocidad(self, velocidad):
        self.Velocidad = velocidad

    def getVelocidad(self):
        return self.Velocidad
    
    def setColor(self, color):
        self.Color = color

    def getColor(self):
        return self.Color
    
    def setMarca(self, marca):
        self.Marca = marca

    def getMarca(self):
        return self.Marca
    
    #esto es para mostrar toda la info en un solo get y no tener que llamar varios get
    def getInfor(self):
        info = "-----------informacion del coche-------------"
        info += "su color es " + self.getColor()
        info += "su velocidad es " + str(self.getVelocidad())
        info += "su marca es " + self.getMarca()

        return info