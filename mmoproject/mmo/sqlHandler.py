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

class Character():
    def __init__(self, charInfo):
        self.id = charInfo[0]
        self.name = charInfo[1]
        self.charClass = charInfo[2]
        self.attribute = charInfo[3]
        self.alliance = charInfo[4]


# Player related queries
def findAccount(account):
    search_query = (f"SELECT * FROM player_account WHERE userName = '{account}'")
    cursor.execute(search_query)
    result = cursor.fetchone()
    if result:
        return Account(result)
    else:
        return None


def findAccountLike(account) -> List[Account]:#find account with simliar name
    search_query = (f"SELECT * FROM player_account WHERE userName LIKE '%{account}%'")
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    accounts = []
    for record in queryResults:
        newAccount = Account(record)
        accounts.append(newAccount)
    return accounts


def CreateAccount(username, email,password):# insert new account into the table
    insert_query = f"INSERT INTO player_account (userName, Player_Email,password) VALUES ('{username}', '{email}','{password}')"
    try:
        cursor.execute(insert_query)
        cnx.commit()
    except:
        cnx.rollback()

# make_friend related queries
def getFriendList(user) -> List[Account]: #return a list of friends
    search_query = f"SELECT Username1 FROM make_friend WHERE Username2 = '{user}' UNION SELECT Username2 FROM make_friend WHERE Username1 = '{user}'"
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    friends = []
    for record in queryResults:
        friends.append(findAccount(record[0]))

    return friends


def insertFriend(user, newFriend):#add friend will call this
    insert_query = f"INSERT INTO make_friend (Username1, Username2) VALUES ('{user}', '{newFriend}')"
    try:
        cursor.execute(insert_query)
        cnx.commit()
    except:
        cnx.rollback()


# inventory related Chris
def findItems(user): #return list of items
    search_query = f"SELECT `character`.nameCharacter, item.ItemName, BagContains.quantity FROM BagContains, HaveBag, inventory, item, `character` WHERE HaveBag.character=`character`.idCharacter AND  HaveBag.bag=inventory.idBag AND inventory.idBag=BagContains.bagid AND BagContains.itemid=item.idItem AND `character`.BelongTo='{user}'"
    cursor.execute(search_query)
    queryResults=cursor.fetchall()
    item=[]
    for result in queryResults:
        item.append( result)
    return item




# Character related queries
def findCharacter(characterName):#take Character nAme return all the info
    search_query = f"SELECT * FROM `character` WHERE nameCharacter = '{characterName}'"
    cursor.execute(search_query)
    result = cursor.fetchone()
    if result:
        return Character(result)
    else:
        return None

def findAllCharacter(user):#takes username
    search_query = f"SELECT * FROM `character` WHERE BelongTo = '{user}'"
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    for result in queryResults:
        print(result)



def CreateCharacter(id, name,Class, Attribute,Alliance, BelongTo):
    insert_query = f"INSERT INTO character (idCharacter, nameCharacter,Class,Atrribute,Alliance,BelongTo) VALUES ('{id}', '{name}','{Class}','{Attribute}','{Alliance}','{BelongTo}',)"
    try:
        cursor.execute(insert_query)
        cnx.commit()
    except:
        cnx.rollback()


def GetSkills(character):#takes character name
    search_query = f"SELECT skill.name,skill.LevelRequirement,skill.value,skill.status FROM `character`,skill WHERE `character`.Class=skill.Class AND `character`.nameCharacter='{character}'"
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    skilllist =[]
    for result in queryResults:
        print(result)
        skilllist.append(result)
    return skilllist