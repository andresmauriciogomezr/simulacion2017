import random
import math

class Montecarlo:

	cantidadPuntos = 1000000000


	def ejecutar(self):
		cantidadAdentro = 0
		for x in xrange(0, self.cantidadPuntos):
			
			x = random.random()
			y = random.random()

			distancia = math.sqrt( math.pow(x,2) + math.pow(y, 2) )
			#print distancia
			if distancia <= 1 :
				cantidadAdentro = cantidadAdentro + 1
		pass		
		#print cantidadAdentro

		pi = (cantidadAdentro / float(self.cantidadPuntos)) * 4
		print "Pi : " + str(pi)

montecarlo = Montecarlo()
montecarlo.ejecutar()