class Artefacto:
	def	__init__(self, nombre, funca, mododeuso, modelo):
		self.nombre= nombre
		self.funca=funca
		self.mododeuso=mododeuso
		self.modelo=modelo
	def decir():
		return f'El/la {self.nombre}, funciona con {self.funca}, es de uso {self.funca} y su modelo es {self.modelo}'
Horno= Artefacto('Horno','gas','manual','artesanal')
Maquinadecoser = Artefacto('Maquinadecoser','electricidad','manual','Precious 590')
Freidoradeaire= Artefacto('Freidoradeaire','electricidad','automatico','Oster2020')



