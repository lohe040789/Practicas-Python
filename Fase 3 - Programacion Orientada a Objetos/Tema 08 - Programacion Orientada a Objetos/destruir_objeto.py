class pelicula: 
    #constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

    #destructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula", self.titulo)

p = pelicula("El Padrino", 175, 1972)
del(p) #borramos la pelicula