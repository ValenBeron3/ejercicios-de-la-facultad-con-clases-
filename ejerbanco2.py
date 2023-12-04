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

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def calcular_total_depositos(self):
        total_depositos = sum(cliente.saldo for cliente in self.clientes)
        return total_depositos

    def mostrar_saldos_clientes(self):
        for cliente in self.clientes:
            cliente.consultar_saldo()


# Creo clientes y agrego al banco
banco = Banco()

while True:
    nombre = input("Ingrese el nombre del cliente (o Enter para salir): ")
    if not nombre:
        break

    saldo_inicial = float(input("Ingrese el saldo inicial del cliente: "))
    cliente = Cliente(nombre, saldo_inicial)
    banco.agregar_cliente(cliente) #agrego a la lista de clientes

# Realizo transacciones por teclado
while True:
    cliente_idx = int(input("Ingrese el número de cliente (1, 2, 3, ...) o 0 para salir: "))
    if cliente_idx == 0:
        break

    cliente = banco.clientes[cliente_idx - 1]
    accion = input("¿Desea realizar una transacción? (depositar/extraer): ").lower()

    if accion == "depositar":
        monto_deposito = float(input("Ingrese el monto a depositar: "))
        cliente.depositar(monto_deposito)
    elif accion == "extraer":
        monto_extraccion = float(input("Ingrese el monto a extraer: "))
        cliente.extraer(monto_extraccion)
    else:
        print("Acción no válida.")

# Muestro saldos y total de depósitos
banco.mostrar_saldos_clientes()
total_depositos = banco.calcular_total_depositos()
print(f"Total de depósitos en el banco: ${total_depositos}")

# Muestro la lista de clientes y sus saldos
print("\nLista de Clientes:")
for i, cliente in enumerate(banco.clientes, start=1):
    print(f"{i}. {cliente.nombre}: ${cliente.saldo}")
