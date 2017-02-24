class Vincent:

	cantidadInicial = 50000
	porcentajeInteres = 10
	cantidadDias = 30

	listaPrestamos = []

	cantidadPrestada = cantidadInicial

	def prestar(self):

		prestamo = Prestamo(self.cantidadInicial, self.porcentajeInteres, self.cantidadDias) #es el prestamo inicial
		self.listaPrestamos.append(prestamo)

		i = 1
		while i < 10:
			cobroDiario = 0
			
			for prestamo in self.listaPrestamos:

				cobroDiario = cobroDiario + prestamo.cobrar()				

				if prestamo.cantidadDias == 0:
					self.listaPrestamos.remove(prestamo)


			print "Se cobro " +  str(cobroDiario)
			self.cantidadPrestada = self.cantidadPrestada + cobroDiario

			nuevoPrestamo = Prestamo(cobroDiario, self.porcentajeInteres, self.cantidadDias)
			self.listaPrestamos.append(prestamo)	
			print "Prestamo " + str(i) + " Se presto " +  str(cobroDiario )+ "	Ahora hay "	+  str(self.cantidadPrestada)

			i = i + 1




class Prestamo:



	def __init__(self, cantidadPrestamo, porcentajeInteres, cantidadDias):

		self.valorCuotaDiaria = (cantidadPrestamo + ((cantidadPrestamo * porcentajeInteres) / 100 )) / 30
		self.cantidadDias = cantidadDias

	
	def cobrar(self):
		self.cantidadDias = self.cantidadDias -1
		return self.valorCuotaDiaria



vincent = Vincent()
vincent.prestar()