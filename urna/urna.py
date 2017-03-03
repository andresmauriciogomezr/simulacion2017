import random

cantidadBlancas = 10
cantidadVerdes = 5
cantidadAzules = 2
totalEsferas = cantidadBlancas + cantidadVerdes + cantidadAzules


aleatorio = random.randrange(1, totalEsferas)
print "primer intento : "

if aleatorio <= cantidadAzules:
	cantidadAzules = cantidadAzules - 1
	print "azul"	
	pass
if aleatorio > cantidadAzules and aleatorio <= cantidadVerdes + cantidadAzules:
	cantidadVerdes = cantidadVerdes - 1
	print "verde"
	pass
if aleatorio > cantidadVerdes and aleatorio <= cantidadBlancas + cantidadVerdes:
	cantidadBlancas = cantidadBlancas - 1
	print "blnca"
	pass

totalEsferas = cantidadBlancas + cantidadVerdes + cantidadAzules
aleatorio = random.randrange(1, totalEsferas)

print "segundo intento : "
if aleatorio <= cantidadAzules:
	cantidadAzules = cantidadAzules - 1
	print "azul"	
	pass
if aleatorio > cantidadAzules and aleatorio <= cantidadVerdes + cantidadAzules:
	cantidadVerdes = cantidadVerdes - 1
	print "verde"
	pass
if aleatorio > cantidadVerdes and aleatorio <= cantidadBlancas + cantidadVerdes:
	cantidadBlancas = cantidadBlancas - 1
	print "blnca"
	pass