from abc import ABC
from abc import abstractmethod
class Personaje_abstract():
	
	@abstractmethod
	def nombre(self):
        pass
    
    @abstractmethod
	def salud(self):
        pass

    @abstractmethod
	def ataque(self):
        pass

    @abstractmethod
	def defensa(self):
        pass
    
    @abstractmethod
	def magia(self):
        pass
    
    @abstractmethod
	def resist_magia(self):
        pass
    
    @abstractmethod
	def daño_critico(self):
        pass

    @abstractmethod
	def alcance_de_ataque(self):
        pass