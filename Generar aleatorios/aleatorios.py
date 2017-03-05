import math
class Aleatorio:

	periodo = []

	def generar(self, semilla, cantidadDeseada):

		i = 0
		while True:
			semilla = semilla * semilla
			numero = self.extraerMitad(semilla, cantidadDeseada)	
			#print semilla		
			if numero in self.periodo :
				break
			else :
				self.periodo.append(numero)
			print numero
			semilla = numero * numero



	"""def extraerMitad(self, numero):
		cantidadDigitos = 1
		
		auxiliar = numero
		while auxiliar > 10:
			auxiliar = auxiliar / 10
			cantidadDigitos = cantidadDigitos + 1

		mitad = cantidadDigitos / 2

		digito = 0
		auxiliar = numero
		for x in xrange(0,mitad):
			digito = auxiliar % 10
			auxiliar = auxiliar / 10
			pass

		resultado = (auxiliar % 10) * 10
		resultado = resultado + digito

		return resultado"""

	def extraerMitad(self, numero, cantidadDeseada):
		cantidadDigitos = 1
		
		auxiliar = numero
		while auxiliar > 10:
			auxiliar = auxiliar / 10
			cantidadDigitos = cantidadDigitos + 1
		auxiliar = numero
		auxiliar = auxiliar / (int)(math.pow(10 , (cantidadDigitos - cantidadDeseada) / 2))
		modulo = auxiliar % math.pow(10, cantidadDeseada)
		print ((int) (modulo))
	

	def congruencial(self, semilla, a, c, m):
		semillas = []
		semillas.append(semilla)
		while True :
			subtotal = a * semilla + c
			residuo = subtotal % m
			resultado = residuo / float(m-1)
			print residuo
			print resultado						
			semilla = residuo

			if semilla in semillas:
				break
			else:
				semillas.append(semilla)

			pass
		
		

aleatorio = Aleatorio()
#aleatorio.extraerMitad(14569375, 3)
#aleatorio.congruencial(4, 5, 7, 8)
aleatorio.generar(1234, 2)
