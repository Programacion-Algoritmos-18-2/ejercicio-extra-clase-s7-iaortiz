class ordenamientoPorInsercion(object):
	# Constructor
	def __init__(self, datos):
		self.datos = datos
	# Método para ordenar por insercion
	def ordenar_insercion(self):
		# Ciclo que itera atravez de length
		for siguiente in range(1, len(self.datos)):
			# Almacenamos el elemento actual
			insercion = self.datos[siguiente]
			# Inicializa ubicación para colocar el elemento
			moverElemento = siguiente
			# Busca un lugar para colocar el elemento actual
			while(moverElemento > 0 and self.datos[moverElemento -1] > insercion):
				# Desplaza el elemento una posición a la derecha
				self.datos[moverElemento] = self.datos[moverElemento - 1]
			self.datos[moverElemento] = insercion
			# Presentación
			print(self.__str__())

	# Método para imprimir la pasada
	def imprimirpasada(self,pasada,indice):
		print("Despues de pasada %2d: "%(pasada))
		for i in range(0,indice):
			print(self.datos[i]+" ")
		print(self.datos+ "* ")

		for i in range(indice+1,len(self.datos)):
			print(self.datos[i]+ " ")
		print("\n")

		for i in range(0,pasada):
			print("-- ")
		print("\n")
	# Presentación
	def __str__(self):
		temporal = " "
		for elemento in self.datos:
			temporal = ("%s %d"%(temporal, elemento))
		temporal = ("%s %s"%(temporal, "\n"))
		return temporal