#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vincent:

	cantidadInicial = 500000
	porcentajeInteres = 10
	cantidadDias = 30

	listaPrestamos = []

	cantidadPrestada = cantidadInicial # Guardará la cantidad total prestada

	cantidadDiasSimulacion = 1080 # determina la cantidad de dìas para las que se harà la simulación 

	prestamoMinimo = 10000 # Cantidad minima para hacer un presamo

	alcanzaMillon = '' # Guardarà la cantidad de días en que se alcanza el millon
	objetivo = 1000000 # Guarda la cantidad objetivo 

	cantidadDiasSinPrestamo = 0


	def prestar(self):

		prestamo = Prestamo(self.cantidadInicial, self.porcentajeInteres, self.cantidadDias) #es el prestamo inicial
		self.listaPrestamos.append(prestamo)
		#print "Prestamo 0 Se presto " +  str(self.cantidadInicial )+ "	Ahora hay "	+  str(self.cantidadPrestada)

		i = 1
		acumuladoCobro = 0 # Se usa para acumular el cobro diario hasta completar 10000

		while i <= self.cantidadDiasSimulacion:
			
			cobroDiario = 0 # Guardará el total que se recoge cada dìa
			
			for prestamo in self.listaPrestamos:
				#print "prestamo de " + str(prestamo.valorCuotaDiaria)
				cobroDiario = cobroDiario + prestamo.cobrar()				

				if prestamo.cantidadDias == self.cantidadDiasSinPrestamo: # ya se pagó todo el prestamo
					self.listaPrestamos.remove(prestamo)

			if cobroDiario >= self.prestamoMinimo: # El acumulado es suficiente para el prestamo
				nuevoPrestamo = Prestamo(cobroDiario, self.porcentajeInteres, self.cantidadDias) # Nuevo prestamo con lo recogido durante el día
				self.listaPrestamos.append(nuevoPrestamo)	

				self.cantidadPrestada = self.cantidadPrestada + cobroDiario
				print "Prestamo " + str(i) + " Se presto " +  str(cobroDiario )+ "	Ahora hay "	+  str(self.cantidadPrestada)
			else:
				acumuladoCobro = acumuladoCobro + cobroDiario


			if acumuladoCobro >= self.prestamoMinimo: # El acumulado es suficiente para el prestamo
				nuevoPrestamo = Prestamo(acumuladoCobro, self.porcentajeInteres, self.cantidadDias) # Nuevo prestamo con lo recogido durante el día
				self.listaPrestamos.append(nuevoPrestamo)	

				self.cantidadPrestada = self.cantidadPrestada + acumuladoCobro
				print "Prestamo " + str(i) + " Se presto " +  str(acumuladoCobro )+ "	Ahora hay "	+  str(self.cantidadPrestada)

				acumuladoCobro = 0
			
			if self.cantidadPrestada >= self.objetivo and self.cantidadPrestada < self.objetivo + ((self.cantidadInicial * 10) /100):
			#if self.cantidadPrestada >= self.objetivo and self.cantidadPrestada < self.objetivo + ((self.objetivo * 0.5) /100):
				self.alcanzaMillon = i


			i = i + 1

		print "En tres años se logró acumular la cantidad de: " + str(self.cantidadPrestada)
		print "se alcanzó el objetivo a los " + str(self.alcanzaMillon) + " dìas"




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
		residuo = self.valorCuotaDiaria % 50
		faltante = 50 - residuo
		self.valorCuotaDiaria = self.valorCuotaDiaria +  faltante



vincent = Vincent()
vincent.prestar()