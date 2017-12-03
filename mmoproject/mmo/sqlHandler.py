import mysql.connector
from mysql.connector import connection
from typing import List

# Initialize MySQL Database connection and cursor
cnx = connection.MySQLConnection(user='root', password='CognitioOccultum0', host='localhost', database='mmoproject')
cursor = cnx.cursor()

class Account():
    def __init__(self, accountInfo):
        self.id = accountInfo[0]
        self.uname = accountInfo[1]
        self.email = accountInfo[2]
        self.password = accountInfo[3]

def findAccount(account):
    search_query = (f"SELECT * FROM mmoproject.mmo_playeraccount WHERE uName = '{account}'")
    cursor.execute(search_query)
    result = cursor.fetchone()
    if result:
        return Account(result)
    else:
        return None

def findAccountLike(account) -> List[Account]:
    search_query = (f"SELECT * FROM mmoproject.mmo_playeraccount WHERE uName LIKE '%{account}%'")
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    accounts = []
    for record in queryResults:
        newAccount = Account(record)
        accounts.append(newAccount)
    return accounts

def findCharacter(characterName):
    search_query = ""