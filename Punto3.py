'''El valor del desempleo en Ibagué aumentó en el primer trimestre un 9.5% y en el segundo
trimestre cayó en un 1.5%. Calcular el valor del desempleo actual.'''
desempleo=float (input("Ingrese el desempleo actual: "))
primerTrimestre=desempleo*0.095
segundoTrimestre=primerTrimestre*0.015
desempleoActual=(desempleo+primerTrimestre)-segundoTrimestre
print (f"El valor del desempleo actual es: {desempleoActual}")
print (f"El valor del desempleo del primer trimestre es: {primerTrimestre}")
print (f"El valor del desempleo del segundo trimestre es: {segundoTrimestre}")



