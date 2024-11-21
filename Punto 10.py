'''. Un atleta tiene la costumbre de medir el tiempo(en minutos) y la distancia (en metros)
durante sus tres días de entrenamiento. Al final de la semana quiere saber el total de
tiempo que duro el entrenamiento , la distancia recorrida, y el promedio del tiempo y la
distancia recorrida.'''
tiempo_total = 0
distancia_total = 0

for dia in range(1, 4):
    tiempo = float(input(f"Digite el tiempo (en minutos) del día {dia}: "))
    distancia = float(input(f"Digite la distancia (en metros) del día {dia}: "))
    tiempo_total += tiempo
    distancia_total += distancia

promedio_tiempo = tiempo_total / 3
promedio_distancia = distancia_total / 3

print(f"Total de tiempo de entrenamiento: {tiempo_total} minutos.")
print(f"Total de distancia recorrida: {distancia_total} metros.")
print(f"Promedio de tiempo por día: {promedio_tiempo} minutos.")
print(f"Promedio de distancia por día: {promedio_distancia} metros.")
