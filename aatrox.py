import personaje_abstract
import personaje_superclass

class Aatrox(Personaje_abstract, Personaje_superclass):

    def __init__(self):
        pass
    
    @property
	def vida(self):
        self._vida
    
    @vida.setter
    def vida(self, vida):
        if isinstance(vida, str)
    
    """
    @abstractmethod
	def reg_vida(self):
        pass

    @abstractmethod
	def armadura(self):
        pass

    @abstractmethod
	def resist_magia(self):
        pass
    
    @abstractmethod
	def vel_mov(self):
        pass
    
    @abstractmethod
	def daño_magia(self):
        pass
    
    @abstractmethod
	def daño_critico(self):
        pass

    @abstractmethod
	def alcance_de_ataque(self):
        pass
    
    """