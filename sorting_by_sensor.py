import json

with open("refactored_data.json") as json_file:
    refactored_data = json.load(json_file)

# Sorting by sensor
sensor = {}
fechas = []
for data in refactored_data:
    temp = sensor.get(data[1])
    temp.append(data[2])
    sensor[data[1]] = temp
    fechas.append(data[0])

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
    for data in sensor:
        temp = sensor[data]
        temp2[data] = temp[i]
    dict_bloque["equipo_ip"] = "172.21.14.13"
    dict_bloque["fecha_hora"] = fechas[i]
    dict_bloque["sensores"] = temp2
    lista_completa.append(dict_bloque)

with open('formatted_data3.json', 'w', encoding='utf-8') as f:
    json.dump(lista_completa, f, ensure_ascii=False, indent=4, default=str)