class Coche:
    color = "negro"
    velocidad = 300
    marca = "ferrare"


    def frenar(self):
        self.velocidad -= 1

    def acelerar(self):
        self.velocidad += 1

    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
coche = Coche()

print(coche.marca, coche.velocidad, coche.color)

coche.setColor("amarillo")

print(coche.marca, coche.velocidad, coche.getColor())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("nueva", coche.velocidad)