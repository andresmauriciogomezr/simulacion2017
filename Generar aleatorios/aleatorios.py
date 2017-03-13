# -*- coding: latin-1 -*-
import math
import matplotlib.pyplot as plot
import numpy as numpy
#from pylab import *

class CuadradosMedios:

	numeros = []

	def generar(self, semilla, cantidadDeseada):

		contadorNumeros = 0
		promedio = 0
		

		while True: # Continúa hasta que encuentre un numero igual en el arreglo

			semilla = semilla * semilla
			
			numero = self.extraerMitad(semilla, cantidadDeseada)
			semilla = numero

			numero = numero / float(math.pow(10, cantidadDeseada))
			
			if numero in self.numeros :
				break
			else :
				self.numeros.append(numero)
				promedio = promedio + numero
				contadorNumeros += 1

				print numero				

		promedio = promedio / contadorNumeros
		print " "
		print "Promedio : " + str(promedio)
		

		desviacion = 0

		for x in xrange(0, len(self.numeros)):
			desviacion = desviacion + math.pow( (self.numeros[x] - promedio), 2 )
			pass

		desviacion = desviacion / float(contadorNumeros - 1)

		varianza = math.sqrt(float(desviacion))

		#print "Desviación : " + str(desviacion)
		print "Varianza : " + str( (varianza) )

		pruebas = Pruebas()
		pruebas.generarHistogramas(self.numeros)
		pruebas.kolgomorov(self.numeros, promedio, varianza)
		
	
	



	def extraerMitad(self, numero, cantidadDeseada):
		cantidadDigitos = 1
		
		auxiliar = numero
		while auxiliar > 10:
			auxiliar = auxiliar / 10
			cantidadDigitos = cantidadDigitos + 1
		auxiliar = numero
		if cantidadDigitos > cantidadDeseada:
			auxiliar = auxiliar / (int)(math.pow(10 , (cantidadDigitos - cantidadDeseada) / 2))
			modulo = auxiliar % math.pow(10, cantidadDeseada)
		else:
			auxiliar = 0
			modulo = 0
		return  ((int) (modulo))
	

class Congruencial:

	def generar(self, semilla, m, a, c):
		pruebas = Pruebas()

		semillas = []
		numeros = [] # Guardara los numeros pseudoaleatorios generados
		semillas.append(semilla)
		
		promedio = 0
		contador = 0
		print "****************************** Numeros *************************************"
		while True :
			subtotal = a * semilla + c
			residuo = subtotal % m
			resultado = residuo / float(m-1)
			
			print resultado
			numeros.append(resultado)
			promedio = promedio + resultado
			contador += 1

			semilla = residuo

			if semilla in semillas:
				break
			else:
				semillas.append(semilla)

			pass
		print "****************************** Numeros *************************************"

		promedio = promedio / float(contador)


		desviacion = 0

		for x in xrange(0, len(numeros)): # Hallamos la desviación de los datos
			desviacion = desviacion + math.pow( (numeros[x] - promedio), 2 )
			pass

		desviacion = desviacion / float(contador - 1)

		varianza = math.sqrt(float(desviacion)) #Calculo de la vairanza

		print " "
		print "****************************************** "
		print "Cantidad Numeros generados : " + str(contador)
		print "Promedio : " + str(promedio)
		print "Varianza : " + str(varianza)
		print "****************************************** "
		print " "
		
		#pruebas.generarHistogramas(numeros)		
		pruebas.kolgomorov(numeros, promedio, varianza)
		

		


class Pruebas:

	def distribucionFrecuencia(self, arreglo, cantidadRangos):
		rango = (1 / float(cantidadRangos))

		resultado = {}
		for x in xrange(1, cantidadRangos+1): #inicializamos el resultado como un diccionario
			resultado[rango * x] = 0
			pass


		for i in xrange(0,len(arreglo)): # Evaluamos cada numero

			for x in xrange(1, cantidadRangos+1): # Calculamos los rango en un diccionario desorenado

				if arreglo[i] >= (rango * (x-1)) and arreglo[i] < (rango * x): # el numero está en el rango
					resultado[rango * x] = resultado[rango * x] + 1
					break

				pass

			pass

		bins = []
		frecuencias = []
		bins.append(0) #Agregamos el valor 0

		for x in xrange(1,len(resultado)+1): # Ordenamos el diccionario resultado
			frecuencias.append( [ (rango * (x)), resultado[rango * (x)] ] ) #[ limite rango, cantidad de numeros en el rango  ]
			bins.append( rango * (x))
			pass
		#print bins
		#print frecuencias		
		return {'bins' : bins, 'tabla' : frecuencias}

	def generarHistogramas(self, numeros):
		

		distribucion1 = self.distribucionFrecuencia(numeros, 5)
		distribucion2 = self.distribucionFrecuencia(numeros, 10)
		distribucion3 = self.distribucionFrecuencia(numeros, 15)
		
		#plot.hist(distribucion)
		#bins = numpy.linspace(0, alpha=0.1)

		plot.subplot(3, 1, 1)
		plot.hist(numeros, bins=distribucion1['bins'], rwidth = 0.2)
		plot.xticks(numpy.arange(0, 1.1, 0.1))
		plot.title('Histogramas')	

		
		plot.subplot(3, 1, 2)
		plot.hist(numeros, bins=distribucion2['bins'], rwidth = 0.2)
		plot.xticks(numpy.arange(0, 1.1, 0.1))

		plot.subplot(3, 1, 3)
		plot.hist(numeros, bins=distribucion3['bins'], rwidth = 0.2)
		plot.xticks(numpy.arange(0, 1.1, 0.1))

		plot.show()

	def kolgomorov(self, numeros, promedio, varianza):
		print "******************************* Kolgomorov ***************************"	
		print " "	
		numeros.sort() # Ordenamos el arreglo para la prueba	

		aleatorios = numpy.random.normal(promedio, varianza, len(numeros)) # Generamos numeros aleatorios con una distribución normal
		
		canridadIntervalos = (int)(math.sqrt(len(numeros)))

		print "************************************"
		print "Cantidad de intervalos : " + str(canridadIntervalos)
		print "************************************"

		frecuencias = self.distribucionFrecuencia(numeros, canridadIntervalos)
		intervalos = frecuencias['tabla'] # [x][0] : rango , [x][1] : Frecuencia relativa

		frecuenciasGeneradas = self.distribucionFrecuencia(aleatorios, canridadIntervalos)['tabla'] # Distribución de frecuencias para los numeros generados con distr normal

		frecObservada = []
		frecObservadaGenerada = []
		for x in xrange(0,len(intervalos)):
			frecObservada.append(intervalos[x][1])
			frecObservadaGenerada.append(frecuenciasGeneradas[x][1])
			pass

		frecRelativa = self.frecuenciaRelativa(frecObservada);
		frecRelAcumulada = self.frecuanciaAcumulada(frecRelativa)

		frecRelativaGenerada = self.frecuenciaRelativa(frecObservadaGenerada); #***************** numeros generados con distribución normal
		frecRelAcumuladaGenerada = self.frecuanciaAcumulada(frecRelativaGenerada)

		diferencia = [] # Diferencia entre distribucion obserada acumulada y esperada acumulada

		for x in xrange(0,len(frecRelativaGenerada)):
			diferencia.append(abs(frecRelAcumulada[x] - frecRelAcumuladaGenerada[x]))
			pass

		print "intervalo 	Limite intv 	Frec Obsrv 	Frec Relat 	FrRel Acum 	FreEsperadaAcum	|FORA - FERA|"
		for x in xrange(0, len(intervalos)):

			print str(x+1) + " 		" + str(float("{0:.2f}".format(intervalos[x][0]))) + " 		" + str(frecObservada[x]) + " 		" + str(float("{0:.4f}".format(frecRelativa[x]))) + " 		" + str(float("{0:.4f}".format(frecRelAcumulada[x]))) + " 		" + str(float("{0:.4f}".format(frecRelAcumuladaGenerada[x]))) + " 		" + str(float("{0:.4f}".format(diferencia[x])))
			pass

		estadistico = max(diferencia)
		nivelSignificancia = 0.05
		gradosLibertad = len(numeros)

		hipotesisTeorica = 1.36 / float(math.sqrt(gradosLibertad))

		print "*********************************************"
		print "Estadistico Kolgomorov : " + str(estadistico)
		print "Nivel de Significancia : " + str(nivelSignificancia)
		print "Grados de libertad : " + str(gradosLibertad)
		print "Hiótesis teórica : " + str(hipotesisTeorica)

		print "**************************************************************************************"

		if hipotesisTeorica > estadistico : # Se acepta la hipotesis
			print "Se acepta la hipótesis de que los números generados por la herramienta tienen una distribución normal"
		else:
			print "No acepta la hipótesis de que los números generados por la herramienta tienen una distribución normal"

		print "**************************************************************************************"

		plot.subplot(211)
		plot.plot(frecRelAcumulada)
		#plot.xticks( numpy.arange( 0, 1.1, ( 1/float( len(intervalos) ) ) ) )
		#plot.hist(distribucionAcumulada, rwidth = 0.2)
		plot.grid(True)
		plot.title('Distribucion de numeros generados por la herramienta')	

		
		plot.subplot(212)
		plot.plot(frecRelAcumuladaGenerada)
		#plot.hist(numeros, bins=distribucion2['bins'], rwidth = 0.2)
		#plot.hist(distribucionAcumuladaAleatorios, rwidth = 0.2)
		plot.grid(True)
		#plot.title('Distribucion normal')	
	

		plot.show()


	def frecuenciaRelativa(self, frecuenciaObservada):

		distribucion = []

		total = 0

		for x in xrange(0, len(frecuenciaObservada)): #Calculamos el todal de numeros
			
			total+= frecuenciaObservada[x]
			#print x / float(len(numeros))
			pass

		for x in xrange(0, len(frecuenciaObservada)): 
			
			#distribucion.append(x / float(len(numeros)))
			distribucion.append(frecuenciaObservada[x] / float(total))
			pass

		return distribucion

	def frecuanciaAcumulada(self, frecuencia):

		acumulada = []
		acumulada.append(frecuencia[0])
		for x in xrange(1,len(frecuencia)):
			acumulada.append(frecuencia[x] + acumulada[x - 1])
			pass
		return acumulada

		
		

cuadrados = CuadradosMedios()
#cuadrados.generar(727, 4)

congruencial = Congruencial()


congruencial.generar(5, 1032, 255, 100) #Caso de prueba 1
#congruencial.generar(5, 1031, 255, 100) #Caso de prueba 2
#congruencial.generar(5, 6075, 106, 1283) #Caso de prueba3
#cuadrados.generar(727, 4) #Caso de prueba4
#cuadrados.generar(128, 4) #Caso de prueba5