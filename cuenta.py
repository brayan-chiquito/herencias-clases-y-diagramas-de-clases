class Cuenta():

    def __init__(self,numeroCuenta,nombre,saldo, numeroOperaciones, MAXIMOREINTEGRO = 500000, cuentasCreadas = 0):
        self.numeroCuenta = numeroCuenta
        self.nombre=nombre
        self.saldo=saldo
        self.numeroOperaciones = numeroOperaciones
        self.MAXIMOREINTEGRO = MAXIMOREINTEGRO
        self.cuentasCreadas = cuentasCreadas
    
    def getnumeroCuenta(self):
        return self.numeroCuenta
    
    def getnombreCuenta(self):
        return self.nombre
    
    def getsaldo(self):
        return self.saldo
    
    def setsaldo(self,valor):
        self.saldo = valor
 
    def getNumeroOperaciones(self):
        return self.numeroOperaciones

    def ingresarCantidad(self,cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
        else:
            print("valor no permitido")

    def retirarCantidad(self,cantidad):
        if cantidad > self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            print("valor no permitido")
    
    def getCuentasCreadas(self):
        return self.cuentasCreadas

    def setCuentasCreadas(self):
        self.cuentasCreadas = self.cuentasCreadas + 1

class CuentaJoven(Cuenta):

    def __init__(self,nombre,saldo=0):
        super().__init__(nombre,saldo)
    
    def ingresarCantidad(self,cantidad):
        if cantidad > 0:
            super().ingresarCantidad(cantidad)
        else:
            print("valor no valido")
    
    def retirarCantidad(self,cantidad):
        if cantidad > self.saldo:
            super().retirarCantidad(cantidad)
        else:
            print("valor no valido")

