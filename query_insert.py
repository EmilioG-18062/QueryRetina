# Retina
# MySQL query insert

import pymysql
import json

# variables to establish connection with MySQL
mysql_host = "localhost"
mysql_user = "user"
mysql_passwd = "passwd"
mysql_db = "database"
mysql_table = "table"

# name of the document to insert in the db
document = "outdated_data.json"


def query_insert(data: list) -> None:
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_db)
    cursor = connection.cursor()

    send = f"INSERT INTO {mysql_table} (retina_sensor_id, valor, sincronizado) VALUES (%s, %s, %s)"
    cursor.executemany(send, data)

    # committing the connection then closing it.
    connection.commit()
    connection.close()


if __name__ == '__main__':
    # open and save data from JSON file
    with open(document) as json_file:
        outdated_data = json.load(json_file)

    sincronizado = 1
    bloque_de_listas = []
    for value in outdated_data:
        fecha = value["fecha_hora"]
        sensores = value["sensores"]
        for sensor in sensores:
            medicion = sensores[sensor]
            lista_mediciones = [fecha, sensor, medicion, sincronizado]
            bloque_de_listas.append(lista_mediciones)

    # comment this line to run test
    query_insert(bloque_de_listas)

    # test / uncomment the lines below to save in a new JSON file the changes in outdated_data
    # with open('refactored_data.json', 'w', encoding='utf-8') as f:
    #   json.dump(refactored_data, f, ensure_ascii=False, indent=4, default=str)
