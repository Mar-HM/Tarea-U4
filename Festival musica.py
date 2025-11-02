
class Artista:
    def __init__(self, nombre: str, genero: str, popularidad: int):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"\n✨ ¡Buenas noches! Es el turno de {self.nombre}, un/a artista de {self.genero} con una popularidad de {self.popularidad}/100.")

    def actuar(self):
        print(f"🎤 {self.nombre} está actuando... ")

    def despedirse(self):
        print(f"👋 ¡Gracias por acompañarnos esta noche, {self.nombre}! ¡El público los despide con un aplauso!")
        print("---") 



class Cantante(Artista):
    def __init__(self, nombre: str, genero: str, popularidad: int, cancion_mas_popular: str):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"🎶 {self.nombre} canta su éxito **{self.cancion_mas_popular}** numero 1 en las listas")

class DJ(Artista):
    def __init__(self, nombre: str, genero: str, popularidad: int, estilo: str):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"🎧 El DJ {self.nombre} mezcla temas de estilo **{self.estilo}**, haciendo vibrar al público.")

class Banda(Artista):
    def __init__(self, nombre: str, genero: str, popularidad: int, integrantes: int):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"🎸 La banda {self.nombre} con **{self.integrantes}** integrantes tocan un gran solo de guitarra.")

def iniciar_festival(lista_artistas: list[Artista]):
    print("\n" + "="*50)
    print("           🌟 ¡COMIENZA EL FESTIVAL! 🌟")
    print("="*50)

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse() 

        print(" Fin de la actuación ") 
        print("="*50) 


if __name__ == "__main__":
    artistas_del_festival = []
    while True:
        try:
            num_artistas = int(input("¿Cuántos artistas se presentarán en el festival? (Ingrese un número): "))
            if num_artistas > 0:
                break
            else:
                print("Por favor, ingrese un número mayor a cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    for i in range(num_artistas):
        print(f"\n--- Datos del Artista #{i+1} ---")
        
        while True:
            tipo_artista = input("Tipo de artista (Cantante, DJ, Banda): ").strip().capitalize()
            if tipo_artista in ["Cantante", "Dj", "Banda"]:
                if tipo_artista == "Dj": 
                    tipo_artista = "DJ"
                break
            print("Tipo no válido. Debe ser 'Cantante', 'DJ' o 'Banda'.")

        nombre = input("Nombre del artista/grupo: ").strip()
        genero = input("Género musical: ").strip()
        
        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                print("La popularidad debe ser un número entre 1 y 100.")
            except ValueError:
                print("Entrada no válida. Ingrese un número entero.")

        
        if tipo_artista == "Cantante":
            cancion = input("Canción más popular: ").strip()
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo_artista == "DJ":
            estilo = input("Estilo de mezcla: ").strip()
            artista = DJ(nombre, genero, popularidad, estilo)
        elif tipo_artista == "Banda":
            while True:
                try:
                    integrantes = int(input("Número de integrantes: "))
                    if integrantes > 0:
                        break
                    print("El número de integrantes debe ser mayor a cero.")
                except ValueError:
                    print("Entrada no válida. Ingrese un número entero.")
            artista = Banda(nombre, genero, popularidad, integrantes)
        
        artistas_del_festival.append(artista)

    
    iniciar_festival(artistas_del_festival)
    
    print("\n🎉 ¡EL FESTIVAL HA TERMINADO! 🎉")