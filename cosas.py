class Alumno:
    facultad = "Fes Aragon"
#constructor
    """def __init__(self):
       self.nombre = "juan"
       self.edad = 20
       self.carrera = "ICO" """

#constructor sobre cargado
    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr