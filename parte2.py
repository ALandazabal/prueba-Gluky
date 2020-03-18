import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='part2gluky',
                                         user='root',
                                         password='')
    
    sql_select_Query = "select * from data_cliente Where meses = 4"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    print(f'Id \t compras \t meses \t estado civil \n')
    for row in records:
        
        print(f'{row[0]} \t {row[1]} \t {row[2]} \t {row[3]} \n')
        '''print("Id = ", row[0], )
        print("compras = ", row[1])
        print("meses  = ", row[2])
        print("estado civil  = ", row[3], "\n")'''

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")