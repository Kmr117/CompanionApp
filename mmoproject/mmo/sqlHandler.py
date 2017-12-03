import mysql.connector
from mysql.connector import connection


cnx = connection.MySQLConnection(user='root', password='CognitioOccultum0', host='localhost', database='mmoproject')
cursor = cnx.cursor()



# print(cursor.execute(searchQuery, account))
acc = str('usr1')
query = ("SELECT * FROM mmoproject.mmo_playeraccount WHERE uName = '%s'")

cursor.execute(query, 'usr1')
print('Cursor executed')
print(cursor.fetchone())