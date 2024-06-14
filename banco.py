class Cuenta:
    def __init__(self, nombre, balance, balance_min):
        self.nombre = nombre
        self.balance = balance
        self.balance_min = balance_min

    def deposito(self, monto):
        self.balance += monto

    def retiro(self, monto):
        if self.balance - monto >= self.balance_min:
            self.balance -= monto
        else:
            print("lo siento, no hay dinero")

    def declaracion(self):
        print("Balance de la cuenta {}".format(self.balance))

class Corriente(Cuenta):
    def __init__(self, nombre, balance):
        super().__init__(nombre, balance, balance_min = -1000)

    def __str__(self):
        return "Cuenta Corriente{} - Balance de {}".format(self.nombre, self.balance)

class Ahorro(Cuenta):
    def __init__(self, nombre, balance):
        super().__init__(nombre, balance, balance_min=0)

    def __str__(self):
        return "Cuenta de Ahorro {} - Balance de {}".format(self.nombre, self.balance)
        
