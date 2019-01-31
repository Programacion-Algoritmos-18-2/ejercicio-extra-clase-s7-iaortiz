class ordenamientoPorSeleccion(object):
	# Constructor
	def __init__(self, datos):
		self.datos = datos
	# Metodo para ordenar por seleccion

	def ordenar_seleccion(self):
		# Ciclo for para recorrer el tamaño de la lista -1
		for i in range(0,len(self.datos) - 1):
			masPequenio = i
			# Ciclo for para recorrer la lista
			for indice in range( i + 1, len(self.datos)):
				# Condicional para encontrar el mas pequeño
				if(self.datos[indice] < self.datos[masPequenio]):
					masPequenio = indice
			# Intercambiamos el mas pequeño en la lissta
			self.intercambiar(i, masPequenio)
			# Presntacion
			print(self.__str__())
	# Método para intercambiar las posiiciones de la lista
	def intercambiar(self, primero, segundo):
		# Alamacenamos el dato en una variable temporal
		temporal = self.datos[primero]
		# Reemplazamos lo que estaba en la variable primera, la reemplazamos por la variable segunda
		self.datos[primero] = self.datos[segundo]
		# El segundo elemento toma el temporal
		self.datos[segundo] = temporal
	# PResentacion
	def __str__(self):
		temporal = " "
		for elemento in self.datos:
			temporal = ("%s	%d" % (temporal, elemento))
		temporal = ("%s %s" % (temporal, "\n"))
		return temporal