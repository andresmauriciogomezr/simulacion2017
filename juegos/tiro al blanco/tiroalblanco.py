import random

class Pista:

	cantidadDisparos = 10000

	cantidadCirculos = 10
	
	def __init__(self):

		self.disparosen1 = 0
		self.disparosen2 = 0
		self.disparosen3 = 0
		self.disparosen4 = 0
		self.disparosen5 = 0
		self.disparosen6 = 0
		self.disparosen7 = 0
		self.disparosen8 = 0
		self.disparosen9 = 0
		self.disparosen10 = 0

	def disparar(self):		
		disparo = random.randrange(0, self.cantidadCirculos)
		if disparo == 0:
			#print "Disparo en " + str(self.cantidadCirculos / self.cantidadCirculos)
			self.disparosen1 = self.disparosen1 +1
			#pass
		if disparo == 1:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*2)
			self.disparosen2 = self.disparosen2 +1
			#pass
		if disparo == 2:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*3)
			self.disparosen3 = self.disparosen3 +1
			#pass
		if disparo == 3:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*4)
			self.disparosen4 = self.disparosen4 +1
			#pass
		if disparo == 4:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*5)
			self.disparosen5 = self.disparosen5 +1
			#pass
		if disparo == 5:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*6)
			self.disparosen6 = self.disparosen6 +1
			#pass
		if disparo == 6:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*7)
			self.disparosen7 = self.disparosen7 +1
			#pass
		if disparo == 7:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*8)
			self.disparosen8 = self.disparosen8 +1
			#pass
		if disparo == 8:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*9)
			self.disparosen9 = self.disparosen9 +1
			#pass
		if disparo == 9:
			#print "Disparo en " + str((self.cantidadCirculos / self.cantidadCirculos)*10)
			self.disparosen10 = self.disparosen10 +1


	def evaluarProbabilidades(self):
		for x in xrange(0,self.cantidadDisparos):
			self.disparar()
			pass

		print "Cantidad de disparos el circulo 1:   " +  str(self.disparosen1)
		print "Cantidad de disparos el circulo 2:   " +  str(self.disparosen2)
		print "Cantidad de disparos el circulo 3:   " +  str(self.disparosen3)
		print "Cantidad de disparos el circulo 4:   " +  str(self.disparosen4)
		print "Cantidad de disparos el circulo 5:   " +  str(self.disparosen5)
		print "Cantidad de disparos el circulo 6:   " +  str(self.disparosen6)
		print "Cantidad de disparos el circulo 7:   " +  str(self.disparosen7)
		print "Cantidad de disparos el circulo 8:   " +  str(self.disparosen8)
		print "Cantidad de disparos el circulo 9:   " +  str(self.disparosen9)
		print "Cantidad de disparos el circulo 10:   " +  str(self.disparosen10)

pista = Pista()
pista.evaluarProbabilidades()
