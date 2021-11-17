import json

# Sorting by sensor
sensor = {}
fechas = []
for var in refactored_data:
    temp = sensor.get(var[1], [])
    temp.append(var[2])
    sensor[var[1]] = temp
    fechas.append(var[0])

# Getting the length of each sensor list
lists_sizes = [len(value) for key, value in sensor.items()]
lists_sizes.sort()

# Make all the lists equal in length
for key in sensor:
    temp = sensor[key]
    temp = temp[:lists_sizes[0]]
    sensor[key] = temp

# Taking rows and packing the data in blocks

lista_completa = []
for i in range(lists_sizes[0]):
    temp2 = {}
    dict_bloque = {}
    for var in sensor:
        temp = sensor[var]
        temp2[var] = temp[i]
    dict_bloque["equipo_ip"] = "172.21.14.13"
    dict_bloque["fecha_hora"] = fechas[i]
    dict_bloque["sensores"] = temp2
    lista_completa.append(dict_bloque)

