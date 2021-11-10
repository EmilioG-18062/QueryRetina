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


def refactor_data(data: list) -> list:
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_db)
    cursor = connection.cursor()

    retrieve = f"SELECT id, retina_sensores FROM {mysql_table}"
    cursor.execute(retrieve)
    result = cursor.fetchall()

    # committing the connection then closing it.
    connection.commit()
    connection.close()

    # changing id and sincronizado value then saving in data
    ref_dict = {str(var[1]): str(var[2]) for var in result}
    for listv in data:
        listv[1] = ref_dict[str(listv[1])]
        listv[3] = 1
    return data


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
    json_file = open(document)
    outdated_data = json.load(json_file)
    json_file.close()

    refactored_data = refactor_data(outdated_data)

    # comment this line to run test
    query_insert(refactored_data)

    # test / uncomment the lines below to save in a new JSON file the changes in outdated_data
    # with open('refactored_data.json', 'w', encoding='utf-8') as f:
    #   json.dump(refactored_data, f, ensure_ascii=False, indent=4, default=str)
