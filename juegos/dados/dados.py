# -*- coding: utf-8 -*-
import random

class Mesa:

	cantidadJuegos = 30 #determina la cantidad de juegos que se realizan para ver cuanto dinero hay en la mesa

	apuestaMinima = 500
	cantidadJugadores = 5
	cantidadGanada = 0
	cantidadPerdida = 0
	#dineroenMesa = 0
	dineroGanado = 0
	jugadores = []	

	def jugar(self):
		dineroenMesa = 0 #Se reinicia el valor de la mesa
		for x in xrange(0,self.cantidadJugadores): #Cobra el inicio de juego a cada jugador			
			jugador = Jugador(x)
			dineroenMesa = dineroenMesa + jugador.pagarPorJugar(self.apuestaMinima)
			self.jugadores.append(jugador)			
			pass

		for x in xrange(0,self.cantidadJugadores): #ronde de apostar
			jugador = self.jugadores[x]
			resultado = jugador.apostar(self.apuestaMinima, dineroenMesa)
			if resultado[0] == 'pierde' :
				dineroenMesa = dineroenMesa + resultado[1]
				print "mesa gana " + str(resultado[1])
				pass
			else:
				dineroenMesa = dineroenMesa - resultado[1]
				print "mesa pierde " + str(resultado[1])				
			pass
		
		print "***************************************************************"
		print "Dinero en mesa al final del juego " +  str(dineroenMesa)
		print "***************************************************************"


		return dineroenMesa

	def evaluarComportamiento(self):
		for x in xrange(0, self.cantidadJuegos):
			print "************************Juego " + str(x +1) + "****************************"
			self.dineroGanado = self.dineroGanado + self.jugar()				
			print " "
			pass 
		print "Dinero ganado por la mesa después de " + str(self.cantidadJuegos) + " juegos es de " + str(self.dineroGanado)




class Jugador:

	cantidadGanada = 0
	cantidadPerdida = 0
	cantidadApostada = 0

	estrategiaAgresiva = False # True significa que los jugadores apuestan el total del dinero en la mesa

	def __init__(self, numeroJugador):
		self.numeroJugador = numeroJugador

	def pagarPorJugar(self, apuestaMinima): #Antes de lanzar el dado
		self.cantidadPerdida = apuestaMinima		
		return apuestaMinima		

	def apostar(self, apuestaMinima, dineroenMesa):		

		primerIntento = self.lanzarDado();
		print "Jugador " + str(self.numeroJugador + 1)
		print "Primer intento " + str(primerIntento)

		if primerIntento == 1 or primerIntento == 6:
			self.cantidadPerdida = apuestaMinima
			return ['pierde', apuestaMinima]
		else :
			if self.estrategiaAgresiva :
				self.cantidadApostada = dineroenMesa
			else:
				self.cantidadApostada = apuestaMinima
			segundoIntento = self.lanzarDado()
			print "segundo intento " + str(segundoIntento)

			if segundoIntento > primerIntento:
				self.cantidadGanada = self.cantidadApostada
				return ['gana', self.cantidadApostada]
			else:
				self.cantidadPerdida = self.cantidadApostada				
				return ['pierde', self.cantidadApostada]





	def lanzarDado(self):
		return random.randrange(1, 7)
		



mesa = Mesa()
mesa.evaluarComportamiento()
