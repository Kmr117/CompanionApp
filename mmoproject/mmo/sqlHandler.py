import mysql.connector
from mysql.connector import connection
from typing import List
from django.db import models

# Initialize MySQL Database connection and cursor
cnx = connection.MySQLConnection(user='root', password='gdbpass', host='localhost', database='gamedatabase')
cursor = cnx.cursor()


class Account():
    def __init__(self, accountInfo):
        self.userName = accountInfo[0]
        self.email = accountInfo[1]
        self.password = accountInfo[2]


# Player related queries
def findAccount(account):
    search_query = (f"SELECT * FROM player_account WHERE userName = '{account}'")
    cursor.execute(search_query)
    result = cursor.fetchone()
    if result:
        return Account(result)
    else:
        return None


def findAccountLike(account) -> List[Account]:
    search_query = (f"SELECT * FROM player_account WHERE userName LIKE '%{account}%'")
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    accounts = []
    for record in queryResults:
        newAccount = Account(record)
        accounts.append(newAccount)
    return accounts


# Character related queries
def findCharacter(characterName):
    search_query = f"SELECT * FROM character WHERE nameCharacter = '{characterName}'"
    cursor.execute(search_query)
    result = cursor.fetchone()
    if result:
        return Account(result)
    else:
        return None


# make_friend related queries
def getFriendList(user) -> List[Account]:
    search_query = f"SELECT Username1 FROM make_friend WHERE Username2 = '{user}' UNION SELECT Username2 FROM make_friend WHERE Username1 = '{user}'"
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    friends = []
    for record in queryResults:
        friends.append(findAccount(record[0]))

    return friends


def insertFriend(user, newFriend):
    insert_query = f"INSERT INTO make_friend (Username1, Username2) VALUES ('{user}', '{newFriend}')"
    try:
        cursor.execute(insert_query)
        cnx.commit()
    except:
        cnx.rollback()