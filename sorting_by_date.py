import json

with open("refactored_data.json") as json_file:
    refactored_data = json.load(json_file)

# Sorting by date
bloques = []
fechas = []
sensores = {}
for data in refactored_data:
    if fechas:
        if data[0] in fechas:
            sensores[data[1]] = data[2]
        else:
            bloque["sensores"] = sensores
            bloques.append(bloque)

            sensores = {}
            bloque = {"fecha_hora": data[0]}
            sensores[data[1]] = data[2]
            fechas.append(data[0])
    else:
        bloque = {"fecha_hora": data[0]}
        sensores[data[1]] = data[2]
        fechas.append(data[0])

with open('formatted_data.json', 'w', encoding='utf-8') as f:
    json.dump(bloques, f, ensure_ascii=False, indent=4, default=str)