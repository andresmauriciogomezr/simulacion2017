import random
import math

class Papel:

	longitudLado = 10
	cantidadAgujas = 100
	longitudAguja = 1

	def lanzar(self):
		for i in xrange(0, self.cantidadAgujas):
			
			x = random.randrange(0, self.longitudLado)
			y = random.randrange(0, self.longitudLado)
			angulo = random.randrange(0, 360)

			xFinal = self.longitudAguja * math.cos(angulo)
			yFinal = self.longitudAguja * math.sin(angulo)
			
			print "X : " + str(x) + " Y : "+ str(y) + " Angulo : " + str(angulo) + " XFinal : "+ str(xFinal) + "YFinal: " + str(yFinal)
			

		pass




papel = Papel()
papel.lanzar()
