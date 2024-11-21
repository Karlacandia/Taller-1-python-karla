'''El sistema de liquidación que hacen los conductores de buses y los colectivos a las
diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro
al terminarlo . La diferencia de estos dos números determina el numero de pasajeros
transportados en el día. Realizar un algoritmo que permita leer estos dos números y el
valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y
el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes
del dinero mientras el conductor recibe el resto.'''
inicio_dia = int(input("Digite el número de la registradora al iniciar el día: "))
fin_dia = int(input("Digite el número de la registradora al finalizar el día: "))
valor_pasaje = float(input("Digite el valor del pasaje: "))

total_pasajeros = fin_dia - inicio_dia
total_recaudado = total_pasajeros * valor_pasaje

liquidado_conductor = total_recaudado * 0.25
liquidado_empresa = total_recaudado * 0.75

print(f"Total de pasajeros transportados: {total_pasajeros}")
print(f"Valor liquidado al conductor: {liquidado_conductor}")
print(f"Total liquidado a la empresa: {liquidado_empresa}")
