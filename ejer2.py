class Cliente:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"{self.nombre} depositó ${cantidad}")
        else:
            print("La cantidad debe ser mayor que cero.")

    def extraer(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"{self.nombre} extrajo ${cantidad}")
        else:
            print("No tiene suficiente saldo para realizar la extracción.")

    def consultar_saldo(self):
        print(f"Saldo de {self.nombre}: ${self.saldo}")


class Banco:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente): #agrego los clientes a la lista vacia
        self.clientes.append(cliente)

    def calcular_total_depositos(self):
        total_depositos = sum(cliente.saldo for cliente in self.clientes)
        return total_depositos

    def mostrar_saldos_clientes(self):
        for cliente in self.clientes:
            cliente.consultar_saldo()


# Creo los clientes 
cliente1 = Cliente("julian", 1000)
cliente2 = Cliente("valentin", 2000)
cliente3 = Cliente("Colorado", 3000)

# los agrego al banco

banco = Banco()
banco.agregar_cliente(cliente1)
banco.agregar_cliente(cliente2)
banco.agregar_cliente(cliente3)

# Realizar transacciones por teclado
monto_deposito = float(input("Ingrese el monto a depositar para el Cliente 1: "))
cliente1.depositar(monto_deposito)

monto_extraccion = float(input("Ingrese el monto a extraer para el Cliente 2: "))
cliente2.extraer(monto_extraccion)

monto_deposito = float(input("Ingrese el monto a depositar para el Cliente 3: "))
cliente3.depositar(monto_deposito)

# Mostrar saldos y total de depósitos
banco.mostrar_saldos_clientes()
total_depositos = banco.calcular_total_depositos()
print(f"Total de depósitos en el banco: ${total_depositos}")

# Mostrar lista de clientes y sus saldos
print("\nLista de Clientes:")
for cliente in banco.clientes:
    print(f"{cliente.nombre}: ${cliente.saldo}")
