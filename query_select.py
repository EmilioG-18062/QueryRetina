# Retina
# MySQL query select

import pymysql
import json

# variables to establish connection with MySQL
mysql_host = "localhost"
mysql_user = "user"
mysql_passwd = "passwd"
mysql_db = "database"

# variables for delimited search within the DB
column_d1 = "estado"
column_d2 = "fecha_hora"
fecha_hora1 = ""
fecha_hora2 = ""


def query_select() -> list:
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_db)
    cursor = connection.cursor()

    retrieve = \
        "SELECT * FROM {database} WHERE ({dateC} BETWEEN {date1} AND {date2}) AND {column}=0".format(database=mysql_db,
                                                                                                     dateC=column_d2,
                                                                                                     date1=fecha_hora1,
                                                                                                     date2=fecha_hora2,
                                                                                                     column=column_d1)
    cursor.execute(retrieve)
    result = cursor.fetchall()

    # committing the connection then closing it.
    connection.commit()
    connection.close()
    return result


if __name__ == '__main__':
    mysql_table = query_select()

    with open('outdated_data.json', 'w', encoding='utf-8') as f:
        json.dump(mysql_table, f, ensure_ascii=False, indent=4)
