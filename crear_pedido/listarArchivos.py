import os
import datetime

file = open("Pedido.txt","w")
total = 0
stringFinal = ''
twomorow = datetime.date.today() + datetime.timedelta(days=1)

precios = {
	'13x18': 7.95,
	'15x21': 9.3,
	'20x30': 25,
	'30x40': 60.25,
	'30x45': 60.25,
}

totalesPorMedidas = {
	'13x18': 0,
	'15x21': 0,
	'20x30': 0,
	'30x40': 0,
	'30x45': 0,
}

stringFinal += "Estimados!"
stringFinal += "\nLes enviamos el nuevo pedido para el " + str(twomorow.strftime('%d/%m/%Y'))
stringFinal += "\n"
stringFinal += "\nSolicitud de Revelado:"
for root, dirs, files in os.walk('./'):
    fotos = len(files)
    if fotos != 0:
    	if len(root) > 2 :
			total += fotos
			lengthStr = str(len(files))
			lengthNum = len(files)
			if lengthNum == 1:
				cadena = lengthStr + " Foto \t\t" + root
			else:
				cadena = lengthStr + " Fotos \t" + root

			if root.find("13x18") >= 0:
				totalesPorMedidas['13x18'] += lengthNum
			if root.find("15x21") >= 0:
				totalesPorMedidas['15x21'] += lengthNum
			if root.find("20x30") >= 0:
				totalesPorMedidas['20x30'] += lengthNum
			if root.find("30x40") >= 0:
				totalesPorMedidas['30x40'] += lengthNum
			if root.find("30x45") >= 0:
				totalesPorMedidas['30x45'] += lengthNum
			
			stringFinal += "\n" + cadena


costoTotal = totalesPorMedidas['13x18'] * precios['13x18'] + totalesPorMedidas['15x21'] * precios['15x21'] + totalesPorMedidas['20x30'] * precios['20x30'] + totalesPorMedidas['30x40'] * precios['30x40'] + totalesPorMedidas['30x45'] * precios['30x45']
cantidadTotal = totalesPorMedidas['13x18'] + totalesPorMedidas['15x21'] + totalesPorMedidas['20x30'] + totalesPorMedidas['30x40'] + totalesPorMedidas['30x45']

stringFinal += "\n"
stringFinal += "\nCantidades Totales:"
stringFinal += "\n13x18 = " + str(totalesPorMedidas['13x18'])
stringFinal += "\n15x21 = " + str(totalesPorMedidas['15x21'])
stringFinal += "\n20x30 = " + str(totalesPorMedidas['20x30'])
stringFinal += "\n30x40 = " + str(totalesPorMedidas['30x40'])
stringFinal += "\n30x45 = " + str(totalesPorMedidas['30x45'])
stringFinal += "\n"
stringFinal += "\nCostos:"
stringFinal += "\n13x18 = " + str(totalesPorMedidas['13x18']) + " por $" + str(precios['13x18']) + " = $" + str(totalesPorMedidas['13x18'] * precios['13x18'])
stringFinal += "\n15x21 = " + str(totalesPorMedidas['15x21']) + " por $" + str(precios['15x21']) + " = $" + str(totalesPorMedidas['15x21'] * precios['15x21'])
stringFinal += "\n20x30 = " + str(totalesPorMedidas['20x30']) + " por $" + str(precios['20x30']) + " = $" + str(totalesPorMedidas['20x30'] * precios['20x30'])
stringFinal += "\n30x40 = " + str(totalesPorMedidas['30x40']) + " por $" + str(precios['30x40']) + " = $" + str(totalesPorMedidas['30x40'] * precios['30x40'])
stringFinal += "\n30x45 = " + str(totalesPorMedidas['30x45']) + " por $" + str(precios['30x45']) + " = $" + str(totalesPorMedidas['30x45'] * precios['30x45'])
stringFinal += "\n"
stringFinal += "\nCosto Total: $"+ str(costoTotal)

if cantidadTotal >= 100:
	costoTotal = costoTotal - (10 * costoTotal / 100)
	stringFinal += "\nDescuento por cantidad -10% = $" + str(costoTotal)

print stringFinal
file.write(stringFinal)
file.close()

print "\nZipeando pedido ...."
execfile("zip.py")
print "\nEliminando Pedido.txt ...."
os.remove('Pedido.txt')
print "Moviendo Pedido.zip a /Solicitud de Revelado en Dropbox ...."
os.rename("Pedido.zip", "C:\Users\manuel.avalos\Dropbox\Solicitud de Revelado\Pedido.zip")
print "\nDone!"