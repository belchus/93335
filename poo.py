#Clase
#Atributos
#Metodos

class Usuario:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad 
    
    def mostrar_perfil(self):
        print("Usuario:",self.nombre)
        print("Edad:",self.edad)

    def presentarse(self):
        print("Hola soy el usuario")

class UsuarioPrivado:
    def __init__(self,nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    

class Administrador(Usuario):

    def eliminar_usuarios(self):
        print("Se eliminaron usuarios del blog..")

    def presentarse(self):
        print("Hola soy el administrador")

class Autor(Usuario):
    def presentarse(self):
        print("Hola soy el autor")

class Post:
    def __init__(self,titulo,autor,visitas):
        self.titulo = titulo
        self.autor = autor
        self.visitas = visitas
        self.estado = "Borrador"
        
    
    def publicar(self):
        self.estado = "Publicado"
        print("El post fue publicado")

    def mostrar_resumen(self):
        print("Titulo:",self.titulo)
        print("Autor:",self.autor)
        print("Estado:",self.estado)

usuario1 = Usuario("Camila",26)
usuario2 = Usuario("Luciano",25)
usuario2.mostrar_perfil()

post1 = Post("Aprendiendo POO","Camila",50)
post1.mostrar_resumen()
post1.publicar()
post1.mostrar_resumen()


admin1 = Administrador("Bautista",23)
admin1.mostrar_perfil()
admin1.eliminar_usuarios()

autor1 = Autor("Diego",24)

usuario1.presentarse()
admin1.presentarse()
autor1.presentarse()

usuario3 = UsuarioPrivado("Julian")
print(usuario3.get_nombre())
usuario3.set_nombre("Julian Matias")
print(usuario3.get_nombre())
