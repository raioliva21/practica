import personaje_abstract

class Personaje_superclass(Personaje_abstract):

    def __init__(self):
        self._nombre = None
		self._salud = None 
		self._ataque = None
        self._defensa = None
        self._magia = None
        self._resistencia_magia = None
