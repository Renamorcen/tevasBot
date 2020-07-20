import discord
import os
from dotenv import load_dotenv
import random

testID = 695026179362783344
realID = 516617064522317835
pragaroID = 726451417342148618
svetainesID = 726451417342148622

#realChebra = [118010837335146511,221331058719850497,430000920231804929,170838541855752192,276381693869424640]
testChebra = [726806470930464768,170838541855752192]
manaID = 170838541855752192
tevoID = 726451652520968292

tekstai = ["Blee-*apsivemia*. Sveiki vakai. Gryzau.",\
        "Kurva mocia ko taip sukauji!?1"]


class Player():
    def __init__(self, ID, name, nick):
        self.ID = ID
        self.nick = nick
        self.name = name
        self.prisisnekejo = 0
        self.mama = False

class Tevas(discord.Client):
    playerlist = []
    activeID = pragaroID
    mama = None
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.init()

    async def on_message(self, message):
        print(message)
        if message.author.id == manaID and type(message.channel) == discord.DMChannel: #As i pm rasau botui. Cia kad jo komandas handlint.
            print("Brolis raso man.")
#        print(message.author.id)
#        print(tevoID)
        if message.guild.id == self.activeID and message.author.id != tevoID:
            print("Kazkas sneka.")
            kiekPrisisnekejo = len(message.content)
            player = self.findPlayer(message.author.id)
            player.prisisnekejo += kiekPrisisnekejo
            print(player.prisisnekejo)
            await self.ieskotMamos()
            
            
#        print(type(message.channel))
#        print(discord.DMChannel)
                    
    async def ieskotMamos(self):
        topPrisisnekejo = 0
        mama = None
        for player in self.playerlist:
            if player.prisisnekejo > topPrisisnekejo:
                topPrisisnekejo = player.prisisnekejo
                mama = player
        if mama == None:
            print("kurva")
        elif self.mama != mama:
            self.mama = mama
            channelis = await self.fetch_channel(svetainesID)
            await channelis.send(tekstai[1])
            await channelis.send("*Tevas susimaise, ir dabar jis galvoja kad {0} yra mama*".format(self.mama.nick))
            


    async def init(self):
        print("Initialising...")
        for guild in self.guilds:
            if guild.id == self.activeID:
                self.playGuild = guild
                for member in guild.members:
                    ID = member.id
                    name = member.name
                    nick = member.nick
                    if nick == None:
                        nick = name
                    self.playerlist += [Player(ID, name, nick)]
        pirmaAukaIndex = random.randint(0,len(self.playerlist)-1)
        self.pirmaAuka = self.playerlist[pirmaAukaIndex]
        await self.introduce()
        print("Init done!")

    async def introduce(self):
        print("Introducing self...")
        channelis = await self.fetch_channel(svetainesID)
        await channelis.send(tekstai[0])
        print("Introduciton done!")

    def findIDByNick(self, nick):
        for player in self.players:
            if player.nick == nick:
                return player.ID
        return None


    def findPlayer(self, ID):
        for player in self.playerlist:
            if player.ID == ID:
                return player
        return None


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
botas = Tevas()
botas.run(token)
