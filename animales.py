class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau Miau")

class Pato(Animal):
    def hacer_sonido(self):
        print("Cuac Cuac")


perro = Perro()
gato = Gato()
pato = Pato()

perro.hacer_sonido()
gato.hacer_sonido()
pato.hacer_sonido()
