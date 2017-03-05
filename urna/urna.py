import random

class Urna:

	def __init__(self):
		self.inicializar()

	def inicializar(self):
		self.cantidadIntentos = 300 # Determina cuantas veces jugar para hallar probabilidades
		
		self.cantidadBlancas = 10
		self.cantidadVerdes = 5
		self.cantidadAzules = 2
		self.totalEsferas = self.cantidadBlancas + self.cantidadVerdes + self.cantidadAzules


	def sacarEsfera(self, aleatorio):
		if aleatorio <= self.cantidadAzules:
			self.cantidadAzules = self.cantidadAzules - 1
			return "azul"	
			pass
		if aleatorio > self.cantidadAzules and aleatorio <= self.cantidadVerdes + self.cantidadAzules:
			self.cantidadVerdes = self.cantidadVerdes - 1
			return "verde"
			pass
		if aleatorio > self.cantidadVerdes + self.cantidadAzules  and aleatorio <= self.cantidadBlancas + self.cantidadVerdes + self.cantidadAzules:
			self.cantidadBlancas = self.cantidadBlancas - 1
			return "blanca"
			pass

	def jugar(self):
		self.inicializar()		
		resultado = {}
		#print self.totalEsferas
		aleatorio = random.randrange(1, self.totalEsferas)
		#print "primer intento : "
		primerIntento = self.sacarEsfera(aleatorio)
		resultado['primerIntento'] = primerIntento

		self.totalEsferas = self.cantidadBlancas + self.cantidadVerdes + self.cantidadAzules
		#print self.totalEsferas
		aleatorio = random.randrange(1, self.totalEsferas)
		#print "segundo intento : "
		segundoIntento = self.sacarEsfera(aleatorio)
		resultado['segundoIntento'] = segundoIntento

		return resultado


	# Objetivo 1: La segunda esfera es verde
	# Objetivo 2: En los dos intentos se optiene una esfera blanca
	# Objetivo 3: La segunda verde, la primera blanca
	def hallarProbabilidad(self):
		cantidadObjetivo1 = 0
		cantidadObjetivo2 = 0
		cantidadObjetivo3 = 0
		for x in xrange(0,self.cantidadIntentos):
			resultado = self.jugar();

			if resultado['segundoIntento'] == 'verde':
				cantidadObjetivo1 = cantidadObjetivo1 + 1
				#break
				pass
			if resultado['primerIntento'] == 'blanca' and resultado['segundoIntento'] == 'blanca' :
				cantidadObjetivo2 = cantidadObjetivo2 + 1
				#break
				pass

			if resultado['primerIntento'] == 'blanca' and resultado['segundoIntento'] == 'verde' :
				cantidadObjetivo3 = cantidadObjetivo3 + 1
				#break
				pass

			pass

		print "Canatidad evento 1 " + str(cantidadObjetivo1)
		print "Canatidad evento 2 " + str(cantidadObjetivo2)
		print "Canatidad evento 3 " + str(cantidadObjetivo3)


urna = Urna()
resultado = urna.hallarProbabilidad()
#print resultado['primerIntento']
#print resultado['segundoIntento']


