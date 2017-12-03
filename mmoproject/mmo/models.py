from django.db import models
# Create your models here.


class PlayerAccount(models.Model):
    uName = models.CharField('Username', primary_key=True, max_length=40)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return "({},{},{})".format(self.uName, self.email, self.password)


class Character(models.Model):
    charID = models.IntegerField(primary_key=True, default=121)
    charName = models.CharField('Character Name', unique=True, max_length=40)
    charClass = models.CharField('Class', default='Warrior',  max_length=20)
    attributes = models.IntegerField(default=5)
    location = models.CharField(default='No location', max_length=20)

    ALLIANCE_CHOICES = (('G', 'GOOD'), ('E', 'EVIL'))
    alliance = models.CharField(choices=ALLIANCE_CHOICES, default='G', max_length=10)


class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField('Item Name',max_length=20)
    desc = models.CharField('Description', default='No description', max_length=100)
    quantity = models.IntegerField(default=1)

class Guild(models.Model):
    guildID = models.AutoField(primary_key=True)
    guildName = models.CharField('Guild Name', max_length=30)
    leader = models.ForeignKey('Character', on_delete=models.CASCADE)
    guildLevel = models.IntegerField(default=1)

class Team(models.Model):
    teamID = models.AutoField(primary_key=True)
    leader = models.ForeignKey('Character', on_delete=models.CASCADE)

