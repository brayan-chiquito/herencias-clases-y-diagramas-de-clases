import math

class Punto :
    coord_x = 0.0
    coord_y = 0.0

    def __init__(self) :
        self.coord_x = 0.0
        self.coord_y = 0.0
    
    def __init__(self, coord_x,  coord_y) :
        self.coord_x = coord_x
        self.coord_y = coord_y
        
    def  getX(self) :
        return self.coord_x
    def setX(self, nueva_coord_x) :
        self.coord_x = nueva_coord_x
    
    def  getY(self) :
        return self.coord_y
    
    def setY(self, nueva_coord_y) :
        self.coord_y = nueva_coord_y

class CircunferenciaCentrada :
    PI = 3.1416
    radio = 0.0
    centro = None
    def __init__(self) :
        self.radio = 0.0
        self.centro = Punto()

    def __init__(self, radio,  coord_x,  coord_y) :
        self.radio = radio
        self.centro = Punto(coord_x, coord_y)

    def  getRadio(self) :
        return self.radio

    def setRadio(self, nuevo_radio) :
        self.radio = nuevo_radio

    def  getDiametro(self) :
        return (2 * self.radio)

    def setDiametro(self, nuevo_diametro) :
        self.radio = nuevo_diametro / 2

    def  getLongitud(self) :
        return (self.radio * 2 * CircunferenciaCentrada.PI)

    def setLongitud(self, nueva_longitud) :
        self.radio = nueva_longitud / (2 * CircunferenciaCentrada.PI)

    def  getArea(self) :
        return (self.radio * self.radio * CircunferenciaCentrada.PI)

    def setArea(self, nuevo_area) :
        self.radio = math.sqrt(nuevo_area) / CircunferenciaCentrada.PI

    def  getXCentro(self) :
        return (self.centro.getX())

    def setXCentro(self, nueva_coord_x) :
        self.centro.setX(nueva_coord_x)

    def  getYCentro(self) :
        return self.centro.getY()

    def setYCentro(self, nueva_coord_y) :
        self.centro.setY(nueva_coord_y)

    def trasladarCircunferenciaCentrada(self, trasl_x,  trasl_y) :
        self.centro.setX(self.centro.getX() + trasl_x)
        self.centro.setY(self.centro.getY() + trasl_y)