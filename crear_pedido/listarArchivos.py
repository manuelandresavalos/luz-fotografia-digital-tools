import os
import datetime
import json

# Le coloco el nombre correcto al txt de Pedido historico
twomorow = datetime.date.today() + datetime.timedelta(days=1)
fileHistoricoTxt = "C:\Users\manuel.avalos\Dropbox\LuzFotografiaDigital\\2018\Historico_de_pedidos\\"+ "Pedido Unicolor " + str(twomorow.strftime('%d-%m-%Y')) + ".txt"
fileHistorico = open(fileHistoricoTxt,"w")

# Levanto la configuracion
config_json = json.loads(open('config.json').read())

total = 0
stringFinal = ''

precios = config_json["precios"];
totalesPorMedidas = config_json["medidas"]

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

			if root.find("9x13") >= 0:
				totalesPorMedidas['13x18'] += lengthNum
			if root.find("10x15") >= 0:
				totalesPorMedidas['13x18'] += lengthNum
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
			if root.find("40x50") >= 0:
				totalesPorMedidas['40x50'] += lengthNum
			if root.find("50x60") >= 0:
				totalesPorMedidas['50x60'] += lengthNum

			stringFinal += "\n" + cadena


costoTotal = totalesPorMedidas['9x13'] * precios['9x13'] + totalesPorMedidas['10x15'] * precios['10x15'] + totalesPorMedidas['13x18'] * precios['13x18'] + totalesPorMedidas['15x21'] * precios['15x21'] + totalesPorMedidas['20x30'] * precios['20x30'] + totalesPorMedidas['30x40'] * precios['30x40'] + totalesPorMedidas['30x45'] * precios['30x45'] + totalesPorMedidas['40x50'] * precios['40x50'] + totalesPorMedidas['50x60'] * precios['50x60']
cantidadTotal = totalesPorMedidas['9x13'] + totalesPorMedidas['10x15'] + totalesPorMedidas['13x18'] + totalesPorMedidas['15x21'] + totalesPorMedidas['20x30'] + totalesPorMedidas['30x40'] + totalesPorMedidas['30x45'] + totalesPorMedidas['40x50'] + totalesPorMedidas['50x60']

stringFinal += "\n"
stringFinal += "\nCantidades Totales:"
stringFinal += "\n9x13 = " + str(totalesPorMedidas['9x13'])
stringFinal += "\n10x15 = " + str(totalesPorMedidas['10x15'])
stringFinal += "\n13x18 = " + str(totalesPorMedidas['13x18'])
stringFinal += "\n15x21 = " + str(totalesPorMedidas['15x21'])
stringFinal += "\n20x30 = " + str(totalesPorMedidas['20x30'])
stringFinal += "\n30x40 = " + str(totalesPorMedidas['30x40'])
stringFinal += "\n30x45 = " + str(totalesPorMedidas['30x45'])
stringFinal += "\n40x50 = " + str(totalesPorMedidas['40x50'])
stringFinal += "\n50x60 = " + str(totalesPorMedidas['50x60'])
stringFinal += "\n"
stringFinal += "\nCostos:"
stringFinal += "\n9x13 = " + str(totalesPorMedidas['9x13']) + " por $" + str(precios['9x13']) + " = $" + str(totalesPorMedidas['9x13'] * precios['9x13'])
stringFinal += "\n10x15 = " + str(totalesPorMedidas['10x15']) + " por $" + str(precios['10x15']) + " = $" + str(totalesPorMedidas['10x15'] * precios['10x15'])
stringFinal += "\n13x18 = " + str(totalesPorMedidas['13x18']) + " por $" + str(precios['13x18']) + " = $" + str(totalesPorMedidas['13x18'] * precios['13x18'])
stringFinal += "\n15x21 = " + str(totalesPorMedidas['15x21']) + " por $" + str(precios['15x21']) + " = $" + str(totalesPorMedidas['15x21'] * precios['15x21'])
stringFinal += "\n20x30 = " + str(totalesPorMedidas['20x30']) + " por $" + str(precios['20x30']) + " = $" + str(totalesPorMedidas['20x30'] * precios['20x30'])
stringFinal += "\n30x40 = " + str(totalesPorMedidas['30x40']) + " por $" + str(precios['30x40']) + " = $" + str(totalesPorMedidas['30x40'] * precios['30x40'])
stringFinal += "\n30x45 = " + str(totalesPorMedidas['30x45']) + " por $" + str(precios['30x45']) + " = $" + str(totalesPorMedidas['30x45'] * precios['30x45'])
stringFinal += "\n40x50 = " + str(totalesPorMedidas['40x50']) + " por $" + str(precios['40x50']) + " = $" + str(totalesPorMedidas['40x50'] * precios['40x50'])
stringFinal += "\n50x60 = " + str(totalesPorMedidas['50x60']) + " por $" + str(precios['50x60']) + " = $" + str(totalesPorMedidas['50x60'] * precios['50x60'])
stringFinal += "\n"
stringFinal += "\nCosto Total: $"+ str(costoTotal)
print stringFinal


if cantidadTotal >= 100:
	costoTotal = costoTotal - (10 * costoTotal / 100)
	print "Descuento por cantidad -10% = $" + str(costoTotal) + "\n"

print "El link de descarga es el siguiente:"
print "https://www.dropbox.com/sh/odwn3hwydnn065t/AAC5nOB8ZiGlQ6_Ap-_G1Lmza?dl=0" + "\n\n\n"

stringFinal += "\n\n-----------------------------------------------"
stringFinal += "\nLista de precios al " + str(twomorow.strftime('%d-%m-%Y')) + ":"
stringFinal += "\n-----------------------------------------------"
stringFinal += "\n9x13 = " + str(precios['9x13'])
stringFinal += "\n10x15 = " + str(precios['10x15'])
stringFinal += "\n13x18 = " + str(precios['13x18'])
stringFinal += "\n15x21 = " + str(precios['15x21'])
stringFinal += "\n20x30 = " + str(precios['20x30'])
stringFinal += "\n30x40 = " + str(precios['30x40'])
stringFinal += "\n30x45 = " + str(precios['30x45'])
stringFinal += "\n40x50 = " + str(precios['40x50'])
stringFinal += "\n50x60 = " + str(precios['50x60'])

fileHistorico.write(stringFinal)
fileHistorico.close()

zipear = raw_input("Zipear y mandar a Solicitud de Revelado? y/n: ")

print "----------------------------------------------------------------------------------------------"
if zipear == 'y':
	print "\nZipeando pedido a ./Pedido.zip...."
	execfile("zip.py")

	print "\nMoviendo Pedido.zip a /Solicitud de Revelado en Dropbox ...."
	os.rename("Pedido.zip", "C:\Users\manuel.avalos\Dropbox\Solicitud de Revelado\Pedido.zip")

print "\nDone!"
print "----------------------------------------------------------------------------------------------"
