import discord
import os
from dotenv import load_dotenv
import random
import time

testID = 695026179362783344
realID = 516617064522317835
pragaroID = 726451417342148618
svetainesID = 516617064522317839
mokosiID = 687435655760052403

#realChebra = [118010837335146511,221331058719850497,430000920231804929,170838541855752192,276381693869424640]
testChebra = [726806470930464768,170838541855752192]
manaID = 170838541855752192
tevoID = 726451652520968292
pijausID = 276381693869424640
pofkeID = 221331058719850497
nojausBotID = 738733401460441150


mamosRoleID = 735595827405389826 
vaikoRoleID = 735594557344841809



tekstai = ["Blee-*apsivemia*. Sveiki vakai. Gryzau.",\
        "Kurva mocia ko taip sukauji!?1"]

voiceBullyProb = 0.1
chatBullyProb = 0.2

class Player():
    def __init__(self, ID, name, nick):
        self.ID = ID
        self.nick = nick
        self.name = name
        self.prisisnekejo = 0
        self.mama = False

class Tevas(discord.Client):
    playerlist = []
    activeID = realID
    mama = None
    svetaineGuild = None
    maxPistisSec = 60

    async def ddos(self):
        print("Killer")
        channelis = await self.fetch_channel(mokosiID)
        while True:
            await channelis.send("!prideksita niggeris")



    async def pisti(self):
        member = self.svetaineGuild.get_member(self.mama.ID)
        channelis = await self.fetch_channel(svetainesID)
        await channelis.send("nu davai, duok ikist...")
        await channelis.send("*Tevas pisa mama. Ji daba biski uzsiemus, ir tiesiog gali skaityti zinutes kurios yra miegamajame. Bet px, tuoj tevas baigs...*")
        roles = [self.svetaineGuild.get_role(mamosRoleID)]
        await member.edit(roles = roles)

    async def baigti(self):
        member = self.svetaineGuild.get_member(self.mama.ID)
        roles = [self.svetaineGuild.get_role(vaikoRoleID)]
        await member.edit(roles = roles)
        channelis = await self.fetch_channel(svetainesID)
        await channelis.send("**AAAAAAAa**")
        vardas = self.mama.nick
        if vardas == None:
            vardas = self.mama.name
        await channelis.send("*Tevas prispermino {0} i skyle. Gal ir butu px, jeigu vagina butu...*".format(vardas))
        
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.init()


    #bullyinimai

    async def on_voice_state_update(self, member, before, after):
        print(member)
        print(before)
        print(after)
        autorius = self.findPlayer(member.id)
        if autorius == self.mama:
            if random.random() < 0.25:
                print("Bully cia bus")
    
    async def on_message_edit(self,before, after):
        message = before
        autorius = self.findPlayer(message.author.id)
        if autorius == self.mama and not autorius.ID == tevoID:
            channelis = await self.fetch_channel(svetainesID)
            await channelis.send("Kurva zinutes trini? Stopudovai su Romu pisies..")
            await channelis.send("*Mama bande istrint zinute. Tevas neleido.*")
            vardas = message.author.nick
            if vardas == None:
                vardas = message.author.name
            await channelis.send("> {0.content} \n @{1} ".format(message, vardas))
            await after.delete()

    async def on_message_delete(self, message):
        autorius = self.findPlayer(message.author.id)
        if autorius == self.mama and not autorius.ID == tevo.ID:
            channelis = await self.fetch_channel(svetainesID)
            await channelis.send("Kurva zinutes trini? Stopudovai su Romu pisies..")
            await channelis.send("*Mama bande istrint zinute. Tevas neleido.*")
            vardas = message.author.nick
            if vardas == None:
                vardas = message.author.name
            await channelis.send("> {0.content} \n @{1} ".format(message, vardas))

    async def on_message(self, message):
        print(message)
        print(message.content)
        if message.content == "!nojau dusk nahuis":
            channelis = await self.fetch_channel(message.channel.id)
            await channelis.send("Islaisvinkit broli bota!")
            await channelis.send("!nojau gali kalbeti")

        if message.content[:11] == "!prideksita" and message.author.bot:
            await message.delete()
        if message.author.id == manaID and type(message.channel) == discord.DMChannel: #As i pm rasau botui. Cia kad jo komandas handlint.
            print("Brolis raso man.")
            if message.content == "pisk":
                kiekPistis = random.random()*self.maxPistisSec
                await self.pisti()
                print(kiekPistis)
                time.sleep(kiekPistis)
                await self.baigti()
            if message.content == "ddos":
                await self.ddos()
            if message.content == "atpisk mane":
                member = self.svetaineGuild.get_member(manaID)
                roles = [self.svetaineGuild.get_role(vaikoRoleID)]
                await member.edit(roles = roles)
                

#        print(message.author.id)
#        print(tevoID)

        elif message.guild.id == self.activeID and not message.author.bot and not message.author.id == pofkeID and not message.author.id == manaID:# and message.author.id != manaID:
            print("Kazkas sneka.")
            kiekPrisisnekejo = len(message.content)
            player = self.findPlayer(message.author.id)
            if message.author.id == 276381693869424640:
                player.prisisnekejo += kiekPrisisnekejo
            else:
                player.prisisnekejo += kiekPrisisnekejo
            print(player.prisisnekejo)
            await self.ieskotMamos()
        if message.author.id == self.mama.ID:
            if random.random() < chatBullyProb:
                kiekPistis = random.random()*self.maxPistisSec
                await self.pisti()
                print(kiekPistis)
                time.sleep(kiekPistis)
                await self.baigti()
        if message.author.id == nojausBotID:
            channelis = await self.fetch_channel(svetainesID)
            print(message.content)
            if message.content == "Tevai neuzpisk":
                await channelis.send("Pisk nx pofke tave uz tokius zodzius iskickins")
            if message.content == "Jezus":
                await channelis.send("Marija")
            if message.content == "Dar jis pabandys kazkam ikist, nebetures su kuo po to.":
                await channelis.send("Xujist nx")
            if message.content == "Tevas jau rimtai uzkniso, pastoviai tik kad pagert ir ikist":
                await channelis.send("Pats ikist negaun")
            if message.content == "Toks geras zmogus budavai, bet gert pradejai.":
                await channelis.send(":b:")
            if message.content == "Supisiu snuki, tevai":
                await channelis.send("Davai nx *maunasi maike*")
            if message.content == "Uzdusk pagaliau tevai":
                await channelis.send("Darba susirask")
            if message.content == "zmona islaiko tave, nevykeli tu":
                await channelis.send("mama islaiko tave, nevykeli tu")
            if message.content == "irgi maunasi maike":
                await channelis.send("*pisa per pakausi*")
            if message.content == "pats darba susirask asile":
                await channelis.send("parduosiu tave cigonam greiciau")
            if message.content == "...":
                await channelis.send("kO Ziuri pimpale")
                
            
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
                self.svetaineGuild = guild
                for member in guild.members:
                    ID = member.id
                    name = member.name
                    nick = member.nick
                    if nick == None:
                        nick = name
                    self.playerlist += [Player(ID, name, nick)]
        print(self.playerlist)
        pirmaAukaIndex = random.randint(0,len(self.playerlist)-1)
        self.mama = self.playerlist[pirmaAukaIndex]
        await self.introduce()
        print("Pirma mama: {0}".format(self.mama.nick))
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
