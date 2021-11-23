# Retina
# MySQL query select

import pymysql
import json
import pysftp
import glob
import os.path

# variables to establish connection with MySQL
mysql_host = "localhost"
mysql_user = "user"
mysql_passwd = "passwd"
mysql_db = "database"
mysql_table1 = "table"
mysql_table2 = "table"

# variables for delimited search within the DB
column_d1 = "sincronizado"
column_d2 = "fecha_hora"
fecha_hora1 = "2021-11-01 00:02:06"
fecha_hora2 = "2021-11-01 07:26:42"

# variables to establish connection with SFTP
myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"
folder_path = r'D:\PycharmProjects\QueryRetina'
file_type = '\*py'


def query_select() -> list:
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_db)
    cursor = connection.cursor()

    retrieve = f"SELECT * FROM {mysql_table1} WHERE ({column_d2} BETWEEN '{fecha_hora1}' AND '{fecha_hora2}') AND {column_d1}=0"
    cursor.execute(retrieve)
    outdated_data = cursor.fetchall()

    retrieve = f"SELECT id, retina_sensores FROM {mysql_table2}"
    cursor.execute(retrieve)
    sensor_id_list = cursor.fetchall()

    # committing the connection then closing it.
    connection.commit()
    connection.close()

    # Converting tuples to list
    data = [list(elem) for elem in outdated_data]

    # changing id and sincronizado value then saving in data
    id_dictionary = {str(sensor_id[0]): str(sensor_id[1]) for sensor_id in sensor_id_list}
    for block in data:
        block[1] = id_dictionary[str(block[1])]
        block[3] = 1

    # Sorting by sensor
    sensor = {}
    fechas = []
    for block in data:
        temp = sensor.get(block[1], [])
        temp.append(block[2])
        sensor[block[1]] = temp
        fechas.append(str(block[0]))

    # Getting the length of each sensor list
    lists_sizes = [len(value) for key, value in sensor.items()]
    lists_sizes.sort()

    # Make all the lists equal in length
    for key in sensor:
        temp = sensor[key]
        temp = temp[:lists_sizes[0]]
        sensor[key] = temp

    # Taking rows and packing the data in blocks
    package_data = []
    for size_value in range(lists_sizes[0]):
        temp2 = {}
        dict_bloque = {}
        for block in sensor:
            temp = sensor[block]
            temp2[block] = temp[size_value]
        dict_bloque["equipo_ip"] = "172.21.14.13"
        dict_bloque["fecha_hora"] = fechas[size_value]
        dict_bloque["sensores"] = temp2
        package_data.append(dict_bloque)

    return package_data


if __name__ == '__main__':
    formatted_data = query_select()

    with open('formatted_data.json', 'w', encoding='utf-8') as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=4, default=str)

    # SFTP connection
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    folder_path = "{0}\\".format(folder_path)
    file = max_file.replace(folder_path, '')

    with pysftp.Connection(myHostname, username=myUsername, password=myPassword) as sftp:
        localFilePath = max_file
        remoteFilePath = f'/var/integraweb-db-backups/{file}'
        sftp.put(localFilePath, remoteFilePath)
