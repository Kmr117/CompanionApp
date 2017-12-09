import mysql.connector
from mysql.connector import connection
from typing import List
from django.db import models

# Initialize MySQL Database connection and cursor
cnx = connection.MySQLConnection(user='root', password='gdbpass', host='localhost', database='gamedatabase')
cursor = cnx.cursor()

#attribute of  entities
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
        self.BelongTo=charInfo[5]
        self.Level=charInfo[6]


class Event():
    def __init__(self, eventInfo):
        self.EventName= eventInfo[0]
        self.EventType= eventInfo[1]
        self.EventDescription = eventInfo[2]
        self.EventNpc= eventInfo[3]


class Guild():
    def __init__(self, guildInfo):
        self.guildName=guildInfo[0]
        self.guildLevel=guildInfo[1]
        self.guildLeader=guildInfo[2]


class Skill():
    def  __init__(self, skillInfo):
        self.SkillName= skillInfo[0]
        self.SkillDamageType=skillInfo[1]
        self.Class= skillInfo[2]
        self.Value=skillInfo[3]


class Item():
    def __init__(self, itemInfo):
        self.itemName=itemInfo[0]
        self.itemCategory=itemInfo[1]
        self.itemDescription=itemInfo[2]
        self.itemValue=itemInfo[3]
        self.quantity=itemInfo[4]



######### MOST RELEVENT QUERIES FOR FRONTEND
def getFriendList(user) -> List[Account]: #return a list of friends
    search_query = f"SELECT Username1 FROM make_friend WHERE Username2 = '{user}' UNION SELECT Username2 FROM make_friend WHERE Username1 = '{user}'"
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    friends = []
    for record in queryResults:
        friends.append(findAccount(record[0]))

    return friends

def InvetoryPage(userName): # to diplay item according to a username, will return 2D array, items[0][0] will return the first character's first item
    characters=findAllCharacter(userName)
    items = []
    for result in characters:
        items.append(findItems(result.name))
    return items

def findAllCharacter(user)->List[Character]:#takes username
    search_query = f"SELECT * FROM `character` WHERE BelongTO = '{user}'"
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    clist=[]
    for result in queryResults:
        C_instance=Character(result)
        clist.append(C_instance)
    return clist

def GetGuildMembers(name):#return a list of character Name that belongs to the Guild
    search_query = f"SELECT * FROM `character` WHERE `character`.InGuild='{name}'"
    cursor.execute(search_query)
    queryResults = cursor.fetchall()
    memberList =[]
    nameList=[]
    for result in queryResults:
        newCharacter = Character(result)
        memberList.append(newCharacter)
    for member in memberList:
        nameList.append(member.name)
    return nameList


def QuestDisplay(userName):# will return 2D array [[1st char quest list],[2nd character quest list]....[n th character quest list]] call get Quest info on each list to get info
    characters=findAllCharacter(userName)
    questlist=[]
    for char in characters:
        questlist.append(GetCharacterQuest(char.id))
    return questlist


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



def insertFriend(user, newFriend):#add friend will call this
    insert_query = f"INSERT INTO make_friend (Username1, Username2) VALUES ('{user}', '{newFriend}')"
    try:
        cursor.execute(insert_query)
        cnx.commit()
    except:
        cnx.rollback()
def deleteFriend(user1,user2): #name of user1 and user2
    delete_query = f"DELETE FROM make_friend WHERE (make_friend.Username1='{user1}' AND Username2='{user2}') OR (make_friend.Username1='{user2}' AND Username2='{user1}')"
    cursor.execute(delete_query)

# inventory related
def findItems(user)->List[Item]: #return list of items
    search_query = f"SELECT  item.ItemName,item.Category,item.Description,item.Attribute, BagContains.quantity FROM BagContains, HaveBag, inventory, item, `character` WHERE HaveBag.character=`character`.idCharacter AND  HaveBag.bag=inventory.idBag AND inventory.idBag=BagContains.bagid AND BagContains.itemid=item.idItem AND `character`.nameCharacter='{user}'"
    cursor.execute(search_query)
    queryResults=cursor.fetchall()
    items=[]
    for result in queryResults:
        newItem=Item(result)
        items.append(newItem)
    return items




 # Character related queries
def findCharacter(characterName):#take Character nAme return all the info
    search_query = f"SELECT * FROM `character` WHERE nameCharacter = '{characterName}'"
    cursor.execute(search_query)
    result = cursor.fetchone()
    if result:
        return Character(result)
    else:
        return None


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


def GetGuildInfo(name):
    search_query = f"SELECT * FROM guild WHERE guild.GuildName = '{name}'"
    cursor.execute(search_query)
    queryResults= cursor.fetchone()
    newGuild = Guild([queryResults[1],queryResults[2], queryResults[4]])
    return newGuild


def GetQuestInfo(id):#get quest information from id of the quest
    search_query = f"SELECT * FROM event WHERE event.idEvent='{id}'"
    cursor.execute(search_query)
    queryResults=cursor.fetchone()
    if queryResults:
        return Event([queryResults[3],queryResults[2],queryResults[1],GetNPCName(queryResults[4])])
    return None


def GetNPCName(id):# get NPC id from id of NPC
    search_query =f"SELECT Name FROM npc WHERE npc.idNPC='{id}'"
    cursor.execute(search_query)
    return cursor.fetchone()


def GetCharacterQuest(id):
    search_query = f"SELECT EventID FROM participate WHERE  CharacterID= '{id}'"
    cursor.execute(search_query)
    query_result = cursor.fetchall()
    questlist = [ ]
    for result in query_result:
        questlist.append(result[0])
    return questlist


def moveItem(fromBag, toBag,itemID):# take id of  bags and id of the item
    update_query_no_item_inToBag =f"UPDATE  BagContains Set bagid='{toBag}' WHERE itemid='{itemID}' AND bagid='{fromBag}'"
    update_query_has_item_inToBag = f"UPDATE BagContains as BG1, BagContains as BG2 SET BG1.quantity=BG1.quantity+BG2.quantity WHERE BG1.itemid=BG2.itemid AND BG1.bagid='{toBag}' AND BG2.bagid='{fromBag}' AND BG2.itemid='{itemID}'"
    remove_Item_query = f" DELETE FROM BagContains WHERE itemid='{itemID}' AND bagid='{fromBag}'"
    cursor.execute(f"SELECT * FROM BagContains WHERE BagContains.itemid='{itemID}'AND BagContains.bagid='{toBag}'")
    query= cursor.fetchone()
    if query:#toBag has the item
        cursor.execute(update_query_has_item_inToBag)
        cnx.commit()
        cursor.execute(remove_Item_query)
        cnx.commit()

    else:
        cursor.execute(update_query_no_item_inToBag)
        cnx.commit()


def getALLBag(UserName): #input username of accout return 2d array  [[all bag ID of 1st character],[all bag ID of 2nd character]......]
    characters=findAllCharacter(UserName)
    baglist=[]
    for chars in characters:
        cursor.execute(f"SELECT bag FROM HaveBag WHERE HaveBag.character='{chars.id}'")
        result = cursor.fetchall()
        baglist.append(result)
    return baglist