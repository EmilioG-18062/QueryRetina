# Retina
# MySQL query insert

import pymysql
import json

# variables to establish connection with MySQL
mysql_host = "localhost"
mysql_user = "user"
mysql_passwd = "passwd"
mysql_database = "database"

# name of the document to insert in the db
document = "outdated_data.json"

# dictionary for refactoring
ref_dict = {"1": "11", "2": "12", "3": "13", "4": "14", "5": "15"}


def refactor_data(data: list) -> list:
    for _list in data:
        temp = ref_dict[str(_list[0])]
        _list[0] = temp
    return data


def query_insert(data: list) -> None:
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_database)
    cursor = connection.cursor()

    send = "INSERT INTO {} (retina_sensor_id, valor, sincronizado) VALUES (%s, %s, %s)".format(mysql_database)
    cursor.executemany(send, data)

    # committing the connection then closing it.
    connection.commit()
    connection.close()


if __name__ == '__main__':
    json_file = open(document)
    outdated_data = json.load(json_file)
    json_file.close()

    refactored_data = refactor_data(outdated_data)

    query_insert(refactored_data)
