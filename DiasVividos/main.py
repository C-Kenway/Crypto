import datetime

# Pedimos la fecha de nacimiento al usuario
fecha_nacimiento = input("Introduce tu fecha de nacimiento (en formato dd/mm/aaaa): ")

# Convertimos la fecha de nacimiento en un objeto datetime
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')

# Calculamos la fecha actual
#fecha_actual = datetime.datetime.now()

# Asignamos la fecha para 8 de marzo 2023
fecha_marzo = ("08/03/2023")
fecha_actual= datetime.datetime.strptime(fecha_marzo, '%d/%m/%Y')

# Calculamos la diferencia entre las dos fechas y la convertimos en días
dias_vividos = (fecha_actual - fecha_nacimiento).days

#Instrucciones
print("\nA la fecha: 08/03/2023")

# Imprimimos el resultado
print("Has vivido {} días.".format(dias_vividos))

valorMod = dias_vividos % 3

print("Te toca el ejercicio: {}".format(valorMod))
