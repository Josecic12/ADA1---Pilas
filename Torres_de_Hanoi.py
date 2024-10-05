class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]

    def __str__(self):
        return str(self.items)

def mover_disco(origen, destino):
    disco = origen.pop()
    destino.push(disco)
    print(f"Mover disco {disco} desde {origen} hasta {destino}")

def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        mover_disco(origen, destino)
    else:
        hanoi(n - 1, origen, destino, auxiliar)
        mover_disco(origen, destino)
        hanoi(n - 1, auxiliar, origen, destino)

torre_origen = Pila()
torre_auxiliar = Pila()
torre_destino = Pila()

for disco in range(3, 0, -1):
    torre_origen.push(disco)

print("Estado inicial:")
print("Origen:", torre_origen)
print("Auxiliar:", torre_auxiliar)
print("Destino:", torre_destino)
print("\nMovimientos:")

hanoi(3, torre_origen, torre_auxiliar, torre_destino)

print("\nEstado final:")
print("Origen:", torre_origen)
print("Auxiliar:", torre_auxiliar)
print("Destino:", torre_destino)
