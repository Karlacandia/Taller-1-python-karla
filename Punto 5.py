'''Hacer un algoritmo que permita determinar las horas a las que equivale una cantidad de
minutos ingresados por el usuario.'''
minutos = int(input("Digite la cantidad de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos equivale a {horas} horas y {minutos_restantes} minutos.")
