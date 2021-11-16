# Retina
# MySQL query select

import pymysql
import json

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
fecha_hora1 = ""
fecha_hora2 = ""


def reformatting_data(data: list) -> list:
    """

    :rtype: object
    """
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_db)
    cursor = connection.cursor()

    retrieve = f"SELECT id, retina_sensores FROM {mysql_table2}"
    cursor.execute(retrieve)
    result = cursor.fetchall()

    # committing the connection then closing it.
    connection.commit()
    connection.close()

    # changing id and sincronizado value then saving in data
    ref_dict = {str(var[0]): str(var[1]) for var in result}
    for listv in data:
        listv[1] = ref_dict[str(listv[1])]
        listv[3] = 1

    data
    return data


def query_select() -> list:
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_db)
    cursor = connection.cursor()

    retrieve = f"SELECT * FROM {mysql_table1} WHERE ({column_d2} BETWEEN '{fecha_hora1}' AND '{fecha_hora2}') AND {column_d1}=0"
    cursor.execute(retrieve)
    result = cursor.fetchall()

    # committing the connection then closing it.
    connection.commit()
    connection.close()
    return result


if __name__ == '__main__':
    outdated_data = query_select()
    formatted_data = reformatting_data(outdated_data)

    with open('formatted_data.json', 'w', encoding='utf-8') as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=4, default=str)
