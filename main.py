# Retina
# MySQL query

import pymysql
import json

# variables to establish connection with MySQL
mysql_host = "localhost"
mysql_user = "user"
mysql_passwd = "passwd"
mysql_database = "database"

# variables for delimited search within the DB
column_d1 = "estado"


def query_select():
    # database connection
    connection = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, database=mysql_database)
    cursor = connection.cursor()

    retrieve = "SELECT * FROM {database} WHERE {column} = 0".format(column=column_d1, database=mysql_database)
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
