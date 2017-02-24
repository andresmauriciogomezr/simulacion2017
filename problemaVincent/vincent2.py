#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vincent:

	cantidadInicial = 500000 
	porcentajeInteres = 10
	cantidadDias = 30

	listaPrestamos = []

	cantidadPrestada = cantidadInicial # Guardará la cantidad total prestada

	cantidadDiasSimulacion = 1080 # determina la cantidad de dìas para las que se harà la simulación 

	def prestar(self):

		prestamo = Prestamo(self.cantidadInicial, self.porcentajeInteres, self.cantidadDias) #es el prestamo inicial
		self.listaPrestamos.append(prestamo)
		#print "Prestamo 0 Se presto " +  str(self.cantidadInicial )+ "	Ahora hay "	+  str(self.cantidadPrestada)

		i = 1
		while i <= self.cantidadDiasSimulacion:
			
			cobroDiario = 0 # Guardará el total que se recoge cada dìa
			
			for prestamo in self.listaPrestamos:
				#print "prestamo de " + str(prestamo.valorCuotaDiaria)
				cobroDiario = cobroDiario + prestamo.cobrar()				

				if prestamo.cantidadDias == 0: # ya se pagó todo el prestamo
					self.listaPrestamos.remove(prestamo)


			self.cantidadPrestada = self.cantidadPrestada + cobroDiario

			nuevoPrestamo = Prestamo(cobroDiario, self.porcentajeInteres, self.cantidadDias) # Nuevo prestamo con lo recogido durante el día
			self.listaPrestamos.append(nuevoPrestamo)	
			
			if self.cantidadPrestada >= 1000000 and self.cantidadPrestada < 1010000:
				print "se alcanzó el millòn a los " + str(i) + " dìas"
			print "Prestamo " + str(i) + " Se presto " +  str(cobroDiario )+ "	Ahora hay "	+  str(self.cantidadPrestada)

			i = i + 1

		print "En tres años se logró acumular la cantidad de: " + str(self.cantidadPrestada)




class Prestamo:



	def __init__(self, cantidadPrestamo, porcentajeInteres, cantidadDias):

		self.valorCuotaDiaria = (cantidadPrestamo + ((cantidadPrestamo * porcentajeInteres) / 100 )) / 30
		self.cantidadDias = cantidadDias
		self.valorPrestamo = cantidadPrestamo
		self.ajustarValorCuota()

	
	def cobrar(self):
		self.cantidadDias = self.cantidadDias -1
		return self.valorCuotaDiaria

	def ajustarValorCuota(self):
		print "valor antes " + str(self.valorCuotaDiaria) 
		residuo = self.valorCuotaDiaria % 50
		faltante = 50 - residuo
		self.valorCuotaDiaria = self.valorCuotaDiaria +  faltante
		print "valor despues " + str(self.valorCuotaDiaria) 



vincent = Vincent()
vincent.prestar()