'''Calcular el área total de un terreno en metros sabiendo que esta fue reducida en un 10%,
y posteriormente, le fue adicionado un 50% con relación al área después de la reducción.'''
terreno = float(input("Digite el área del terreno: "))
reducido = terreno * 0.10
area_reducida = terreno - reducido
adicion = area_reducida * 0.50
area_terreno_total = area_reducida + adicion
print("El área total del terreno después de la reducción y adición es:", area_terreno_total)
