import os
import discord
import random
import mimetypes
from discord import channel
from discord.ext import commands
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import shutil

intents = discord.Intents().all()
client= commands.Bot(command_prefix="$", intents=intents)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Artist')
    await member.add_roles(role)



#compare string
from decimal import *
class CharPairs:
    def __init__(self, string):
        self.string = string.lower()
        self.create_char_list()
        self.create_char_pairs()
        
    def create_char_list(self):
        self.str_length = 0
        self.strChars = {}
        for char in self.string:
            self.strChars[self.str_length] = char
            self.str_length += 1
    
    def create_char_pairs(self):
        self.charPairs = []
        self.charPairCount = 0
        count = 0
        for char in self.strChars:
            if count < (self.str_length -1):
                y = count + 1
                pair = self.strChars[count] + self.strChars[y]
                self.charPairs.append(pair)
                self.charPairCount += 1
                
            count += 1
    
    def getCharPairs(self):
        return self.charPairs
        
    def getCharPairCount(self):
        return self.charPairCount 
#Word Similarity Algorithm
#Similarity(string1, string2) = 2 * number of incommon char. pairs / sum of total number of char. pairs in each string
class similarity:
    def __init__(self,string1, string2):
        #get character pairs for string1
        strChar1 = CharPairs(string1)
        self.charPair1 = strChar1.getCharPairs()
        self.charPair1Count = strChar1.getCharPairCount()
        self.string1 = string1.lower()
        #get character pairs for string2
        strChar2 = CharPairs(string2)
        self.charPair2 = strChar2.getCharPairs()
        self.charPair2Count = strChar2.getCharPairCount()
        self.string2 = string2.lower()
        #run steps
        self.find_in_common_char_pairs()
        self.calculate_similarity()
        
    def find_in_common_char_pairs(self):
        self.incommon = set(self.charPair1).intersection(self.charPair2)
        self.incommon_count = 0
        for i in self.incommon:  
            self.incommon_count += 1
    
    def calculate_similarity(self):
        numerator = 2 * self.incommon_count
        denominator = self.charPair1Count + self.charPair2Count
        getcontext().prec = 4
        self.sim = Decimal(numerator) / Decimal(denominator)
        
    def get_sim(self):
        return self.sim
class Compare:
    def compare_string(answer,info):
        answerLs = answer.split()
        stringLs = info.split()
        score = 0
        for answerWord in answerLs:
            max = 0
            for string in stringLs:
                tempScore = similarity(answerWord, string).get_sim()
                if tempScore>max:
                    max = tempScore
            score = score + max
        score = score/len(answerLs)
        return score







off = False

#oc inspire
species = ['elf', 'human', 'dragon', 'mermaid', 'alien', 'demon', 'angel', 'goddess', 'fairy', 'orc', 'robot','cat girl']
cloth = ['1500s','preppy','goth','punk','futuristic','hippie','1960s','lazy','cute','1800s','superhero','emo','oversized','ancient','naked(XD)','athletic','trash','royal','sexy','early 2000s','adventurer','jail','school']
color = ['red','almond','amanranth','amethyst','aqua','grey','azure','pink','golden-pink','black','blonde','chocolate','lavender','rose','cyan','amazon']
accessory = ['glassed','horn','cat-tail','bandadge','guitar', 'sword', 'stockings','shuriken','bunny ears', 'meowbot', 'mask','tentacles']
encorageEmoji = ['<:nagatorosmile:861802547286114325>','👍','♥️','✨','💖','🔥']

#anime master
images = ['https://cdn.myanimelist.net/images/characters/4/277146.jpg','https://cdn.myanimelist.net/images/characters/2/241413.jpg','https://cdn.myanimelist.net/images/characters/10/249647.jpg','https://cdn.myanimelist.net/images/characters/9/310307.jpg','https://cdn.myanimelist.net/r/50x78/images/characters/6/122643.webp?s=ea1349faa1d051356b7efd363c1eb2ca','https://cdn.myanimelist.net/images/characters/6/63870.jpg','https://cdn.myanimelist.net/images/characters/3/100534.jpg','https://cdn.myanimelist.net/images/characters/9/72533.jpg','https://cdn.myanimelist.net/images/characters/10/114399.jpg','https://cdn.myanimelist.net/images/characters/9/215563.jpg','https://cdn.myanimelist.net/images/characters/4/203555.jpg','https://cdn.myanimelist.net/images/characters/10/216895.jpg','https://cdn.myanimelist.net/images/characters/9/311327.jpg','https://cdn.myanimelist.net/images/characters/9/251339.jpg','https://cdn.myanimelist.net/images/characters/11/294388.jpg','https://cdn.myanimelist.net/images/characters/7/284129.jpg','https://cdn.myanimelist.net/images/characters/4/50197.jpg','https://cdn.myanimelist.net/images/characters/7/204821.jpg','https://cdn.myanimelist.net/images/characters/3/328158.jpg','https://cdn.myanimelist.net/images/characters/11/287902.jpg','https://cdn.myanimelist.net/images/characters/14/349249.jpg','https://cdn.myanimelist.net/images/characters/6/252863.jpg','https://cdn.myanimelist.net/images/characters/3/174561.jpg','https://cdn.myanimelist.net/images/characters/7/72983.jpg','https://cdn.myanimelist.net/images/characters/12/426446.jpg','https://cdn.myanimelist.net/images/characters/10/352557.jpg','https://cdn.myanimelist.net/images/characters/10/46644.jpg','https://cdn.myanimelist.net/images/characters/2/366639.jpg','https://cdn.myanimelist.net/images/characters/6/275276.jpg','https://cdn.myanimelist.net/images/characters/5/280576.jpg','https://cdn.myanimelist.net/images/characters/8/241475.jpg','https://cdn.myanimelist.net/images/characters/15/262053.jpg','https://cdn.myanimelist.net/images/characters/3/148437.jpg','https://cdn.myanimelist.net/images/characters/15/319492.jpg','https://cdn.myanimelist.net/images/characters/5/307236.jpg','https://cdn.myanimelist.net/images/characters/15/74607.jpg','https://cdn.myanimelist.net/images/characters/3/299595.jpg','https://cdn.myanimelist.net/images/characters/3/89190.jpg','https://cdn.myanimelist.net/images/characters/9/131317.jpg','https://cdn.myanimelist.net/images/characters/16/308364.jpg','https://cdn.myanimelist.net/images/characters/9/345616.jpg','https://cdn.myanimelist.net/images/characters/7/299404.jpg','https://cdn.myanimelist.net/images/characters/12/313152.jpg']
info = ['Lelouch Lamperouge Code Geass','levi attack on titans shingeki no kyojin','L Lawliet death note','Luffy Monkey D. one piece','okabe rintarou steins gate','light yagami death note','zoro roronoa one piece', 'edward elric fullmetal alchemist', 'kurisu makise steins gate', 'Mikasa Ackerman attack on titans shingeki no kyojin','Hachiman Hikigaya Yahari Ore no Seishun Love Comedy wa Machigatteiru.','Eren Yeager attack on titans shingeki no kyojin','Rem Re Zero','kaneki ken tokyo ghoul','saitama one punch man','hatake kakashi naruto','spiegel spike cowboy bebop','kirigaya kazuto sword art online SAO','yato naragami','senjougahara hitagi bakemonogatari','megumin konosuba','joestar joseph JOJO','morrow hisoka hunterxhunter','mustang roy fullmetal alchemist','gojou satoru jujutsu kaisen','zero two darling in the franXX','aisaka taiga toradora','Mai Sakurajima Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai','Saber Fate Stay Night','Gasai Yuno Mirai Nikki','Onizuka Eikichi Great Teacher Onizuka','Yuki Asuna Sword Art Online SAO','Araragi Koyomi Bakemonogatari','Holo Ookami to Koushinryou','Dazai Osamu Bungou Stray Dogs','Alucard Hellsing','Todoroki Shouto My Hero Academia','Kurosaki Ichigo Bleach','Uchiha Sasuke Naruto','Reigen Arataka Mob Pyscho 100','Evergarden Violet','Midoriya Izuku My Hero Academia','Orihara Izaya Durarara!!']
gamePlayer = 0
gameChannel = 0
answer = -1
pts = 0
replaceStr = ''

def attachIsImage(msgAttach):
    url = msgAttach.url
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

@client.event
async def on_ready():
    print('All ready!')

@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "Artist") 
    await ctx.add_roles(role)

@client.event
async def on_message(message):
    global answer
    global off
    global gameChannel
    global gamePlayer 
    if message.author == client.user:
        return
    
    if message.content.startswith('-restart'):
        off = False
        await message.channel.send('Hello Meow!')

    if off:
        return

    if message.content.startswith('-r '):
        if message.content.startswith('-r feet') or message.content.startswith('-r foot'):
            await message.channel.send('https://i.pinimg.com/736x/5d/e2/82/5de282aaa62482be79f95f8ad2dc5894.jpg')
            await message.channel.send('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a6843f1a-bf5a-490a-8c5d-ce6f92811539/d5bklly-e491feaf-acf1-4afe-82ac-4220a0c39e41.jpg/v1/fill/w_900,h_651,q_75,strp/feet_reference_by_kibbitzer_d5bklly-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjUxIiwicGF0aCI6IlwvZlwvYTY4NDNmMWEtYmY1YS00OTBhLThjNWQtY2U2ZjkyODExNTM5XC9kNWJrbGx5LWU0OTFmZWFmLWFjZjEtNGFmZS04MmFjLTQyMjBhMGMzOWU0MS5qcGciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.Px9Q69OMylfmochRcjrIkmz_oxhgWFE2KVplBKxV_Ws')
            await message.channel.send('https://images.squarespace-cdn.com/content/v1/54fc8146e4b02a22841f4df7/1506856147725-7HF1AXXW31MBDF4OY1WG/55a5f1fb72447614c130e339c89de923.jpg')
        if message.content.startswith('-r folds') or message.content.startswith('-r clothing folds'):
            await message.channel.send('https://www.clipstudio.net/how-to-draw/archives/157926')
            await message.channel.send('https://i.pinimg.com/originals/29/47/28/294728b02ced7d501c112bbf3d90591d.jpg')
            await message.channel.send('https://drawingref.com/wp-content/uploads/2019/11/Clothing_folds3.jpg')
        if message.content.startswith('-r hand'):
            await message.channel.send('https://i.pinimg.com/736x/a1/67/65/a16765a8fd1a792c5173526dbbaa6c17.jpg')
            await message.channel.send('https://i.pinimg.com/originals/8b/ce/22/8bce222a710e6a7eaceba69ecc6fa516.png')
            await message.channel.send('https://i.pinimg.com/474x/d3/a9/66/d3a9668a28efa7b859ed581779f3e113.jpg')
        if message.content.startswith('-r eye'):
            await message.channel.send('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e85e5f6d-adc3-4fbc-9a9c-e3a817e0e0a1/dd8mtwf-94fc35c9-593b-4782-aaf5-75d23569a3c2.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2U4NWU1ZjZkLWFkYzMtNGZiYy05YTljLWUzYTgxN2UwZTBhMVwvZGQ4bXR3Zi05NGZjMzVjOS01OTNiLTQ3ODItYWFmNS03NWQyMzU2OWEzYzIuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.-GuCULgm9z34mnt2A_mQnjcV0gerTRuJBJ7lBmFxFhg')
            await message.channel.send('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/946e0913-0dc0-4a66-b8f2-150d96b9c6e4/d348h51-0d434dde-0f26-4222-be06-4d0acc06265c.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk0NmUwOTEzLTBkYzAtNGE2Ni1iOGYyLTE1MGQ5NmI5YzZlNFwvZDM0OGg1MS0wZDQzNGRkZS0wZjI2LTQyMjItYmUwNi00ZDBhY2MwNjI2NWMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.W5VttIlh5adSs2mPNNSR0zQznQx7B8RQ7Gb9B3dHMHM')
            await message.channel.send('https://i.pinimg.com/originals/04/30/4b/04304ba218dc3ffc31df8520748ecbc9.jpg')

    if message.content.startswith('-command') or message.content.startswith('-help') or message.content.startswith('-info'):
      await message.channel.send('All commands start with -(minus sign)!\nYou can try greeting with -hello!\n\nList of commands: \n\n1.-command/-help/-help: show all commands available\n\n2.-oc: give ideas of original character design\n\n3.-shut down/-restart: disable/enable meowbot\n\n4.-r + feet/eye/folds/hand for references\n\n5.-play: play anime master game!\n\n6.-inspire + (anything) to get an art of the thing you specified! (eg. -inspire bunny suit)\n\n7. -saveas (name) to save your art!\nalso you can use -save to save it with default name (not recommended)\n-gallery to view all your arts\n-gallery -7 to view all your arts in July or\n-gallery -7/17 to view your art on this specific date\n-remove -7 to delete all july arts\n-remove -7/17 to delete all arts on this day\n( :warning: the art deleted can\'t be recovered, so be careful when using -remove command!!! :warning: )')

    if message.content.startswith('-oc'):
      await message.channel.send('hmmmmmm...\nwhat about **' + random.choice(species) + '** with **'+random.choice(color)+'** hairs, **'+ random.choice(cloth)+'** clothes, and with **' + random.choice(accessory)+'**?')

    if message.content.startswith('-hello'):
        await message.channel.send('Meow!')

    if message.content.startswith('-shut down'):
        off = True
        await message.channel.send('QwQ shutting down...')
        await message.channel.send('<:kat:709596572333375499>')

    if message.content.find('good night') != -1:
        await message.channel.send('Oyasumi~!')

    if message.content.find('good morning') != -1:
        await message.channel.send('Ohayo~!')

    if message.content.find('shut up') != -1 or message.content.find('fuck') != -1 or message.content.find('shit') != -1:
        await message.channel.send('Rude :3')

    if message.content.find('-showlist') != -1:
        for x in range(0,len(info)):
            await message.channel.send(info[x])
            await message.channel.send(images[x])

    if (len(message.attachments) > 0):
        for x in range(0,len(message.attachments)):
            if (attachIsImage(message.attachments[x])):
                await message.add_reaction(random.choice(encorageEmoji))

    if message.content.find('-add role') != -1:
        role = discord.utils.get(message.author.guild.roles, name='Artist')
        await message.author.add_roles(role)

    if message.channel.id == 709509377320812624:
        await message.add_reaction('👋')

    if message.type == discord.MessageType.new_member:
        await client.get_channel(709517712820404354).send("Welcome " + message.author.name + "!\nWe're glad you're here! :heart: This is a warm and cozy place for artists that love animes! :kissing_heart: \nIf you have any arts that want to share with us, please post at #art-dump\n :warning: Remember to read the important rules and guidelines in #❌very-important-rules❌ before posting!!! :warning: \nWe hope you have a great time here ^^")

    if message.content.startswith('-vibe'):
        await message.channel.purge(limit = 1)
        await message.channel.send('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/28507ac7-8043-4476-a6fd-6cade4a29995/ddkgqs9-84c40db9-4461-42b1-bc9c-0dd9e1418820.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI4NTA3YWM3LTgwNDMtNDQ3Ni1hNmZkLTZjYWRlNGEyOTk5NVwvZGRrZ3FzOS04NGM0MGRiOS00NDYxLTQyYjEtYmM5Yy0wZGQ5ZTE0MTg4MjAuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.v86Tv6dVM5Ll6bSR8V-BkUT6KOO_t0dl3aQWxsShci8')

    if message.content.startswith('-inspire'):
        siteUrl = 'https://www.deviantart.com/search?q=' + message.content[9:len(message.content)]
        siteUrl.replace(' ','%20')
        response = requests.get(siteUrl)
        soup = BeautifulSoup(response.text, 'html.parser')
        linkList = []
        for a in soup.find_all('a', href=True):
            if a['href'].find('/art/')!=-1 and a['href'].find('#comments') == -1:
                linkList.append(a['href'])
        link = random.choice(linkList)
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        for img in soup.find_all('img'):
            if(img['src'].find('images-wixmp') != -1):
                await message.channel.send(img['src'])
                break

    if message.content.find('-saveas') != -1:
        id = message.author.id
        dataPath = '\data\\' + str(id)
        format = '.jpg'
        if not os.path.isdir(dataPath):
            os.mkdir(dataPath)
        name = message.content[8:len(message.content)]
        name.replace(' ','_')
        attachmentUrl = ''
        try:
            attachmentUrl = message.attachments[0].url
        except IndexError:
            await message.channel.send('No attachments found meow!')
        else:
            if attachmentUrl[0:26] == 'https://cdn.discordapp.com':
                if attachmentUrl.find('png') != -1:
                    format = '.png'
                r = requests.get(attachmentUrl, stream=True)
                now = datetime.now()
                imageName = dataPath + '\\' + now.strftime("%m") +'_' + now.strftime("%d") + ' ' + name + format
                with open(imageName,'wb') as out_file:
                    shutil.copyfileobj(r.raw,out_file)
                await message.channel.send('Art saved successfully! Use -gallery -' + now.strftime('%m') +'/'+now.strftime('%d')+' command to check your saved art!')
    elif message.content.find('-save') != -1:
        id = message.author.id
        dataPath = '\data\\' + str(id)
        format = '.jpg'
        if not os.path.isdir(dataPath):
            os.mkdir(dataPath)
        now = datetime.now()
        name = now.strftime('%H') + '_' + now.strftime('%M') + '_' + now.strftime('%S')
        attachmentUrl = ''
        try:
            attachmentUrl = message.attachments[0].url
        except IndexError:
            await message.channel.send('No attachments found meow!')
        else:
            if attachmentUrl[0:26] == 'https://cdn.discordapp.com':
                if attachmentUrl.find('png') != -1:
                    format = '.png'
                r = requests.get(attachmentUrl, stream=True)
                imageName = dataPath + '\\' + now.strftime("%m") +'_' + now.strftime("%d") + ' ' + name + format
                with open(imageName,'wb') as out_file:
                    shutil.copyfileobj(r.raw,out_file)
                await message.channel.send('Art saved successfully! Use -gallery -' + now.strftime('%m') +'/'+now.strftime('%d')+' command to check your saved art!')

    if message.content.startswith('-gallery'):
        content = message.content[8:len(message.content)]
        if message.content.find('-') != -1:
            content = content[content.find('-')+1:len(content)]
            content = content.replace('/','_')
            content = content.replace('.','_')
            if content.find('_') == 1:
                content = '0' + content
        else:
            content = 'NULL'
        id = message.author.id
        dataPath = '\data\\' + str(id)
        if not os.path.isdir(dataPath):
            await message.channel.send('You don\'t have any works saved currently, try using -save or -saveas (name)!')
            return
        files = [f for f in os.listdir(dataPath)]
        count = 0
        for art in files:
            if content != 'NULL' and not art.startswith(content):
                continue
            blankIndex = art.find(' ')
            date = art[0:blankIndex].replace('_','/')
            name = art[blankIndex+1:len(art)-4]
            await message.channel.send('date: ' + date + ' name: ' + name)
            with open(dataPath+'\\' + art,'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
                count += 1
        if count == 0:
            await message.channel.send('No data on this date/month :3')

    if message.content.startswith('-remove'):
        content = message.content[7:len(message.content)]
        if message.content.find('-') != -1:
            content = content[content.find('-')+1:len(content)]
            content = content.replace('/','_')
            content = content.replace('.','_')
            if content.find('_') == 1:
                content = '0' + content
        else:
            content = 'NULL'
        id = message.author.id
        dataPath = '\data\\' + str(id)
        if not os.path.isdir(dataPath):
            await message.channel.send('You don\'t have any works saved currently, try using -save or -saveas (name)!')
        files = [f for f in os.listdir(dataPath)]
        count = 0
        for art in files:
            if content != 'NULL' and art.startswith(content):
                os.remove(dataPath + '\\' + art)
                count+=1
        await message.channel.send(str(count) + ' arts successfully removed!')


    # no more code below
    global pts
    global replaceStr
    data = ''
    if message.content.startswith('-score'):
        await message.channel.send('Your score is: ' + str(pts))
        return
    if message.content.startswith('-play'):
        await message.channel.send('Welcome to anime master! type **-ready** to start the game! **-end/-stop** to end the game!')
    if message.content.startswith('-end') or message.content.startswith('-stop'):
        WgameData = open("\gameData.txt",'w')
        RgameData = open("\gameData.txt",'r')
        data = RgameData.read()
        if data.find(replaceStr) == -1 or len(replaceStr) == 0:
            data = data + '('+str(gamePlayer)+':' + str(pts) + ')'
        else:
            data.replace(replaceStr,'('+str(gamePlayer)+':' + str(pts) + ')')
        WgameData.truncate(0)
        WgameData.write(data)
        WgameData.flush()
        gamePlayer = 0
        gameChannel = 0
        answer = -1
        await message.channel.send('Thanks for playing! :3')
    if message.content.startswith('-ready'):   
        gameData = open("\gameData.txt",'r')    
        gamePlayer = message.author.id
        gameChannel = message.channel.id
        data = gameData.read()
        if data.find('('+str(gamePlayer)+':') == -1:
            pts = 0
            replaceStr = ''
        else:
            begin = data.find('('+str(gamePlayer)+':')
            data = data[begin:len(data)]
            scoreBegin = data.find(':')+1
            scoreEnd = data.find(')')
            data = data[scoreBegin:scoreEnd]
            pts = int(data)
            replaceStr = '('+str(gamePlayer)+':' + str(pts) + ')'
    if gamePlayer!=0 and gameChannel!=0 and message.channel.id == gameChannel and message.author.id == gamePlayer and answer != -1:
        score = Compare.compare_string(message.content,info[answer])
        if score == 1:
            await message.channel.send('correct meow!')
            pts = pts + 3
        elif score >= 0.5:
            await message.channel.send('mostly correct but seems a bit off meow!')
            pts = pts + 2
        elif score >= 0.1:
            await message.channel.send('seems not correct meow!')
        else:
            await message.channel.send('no :3')
            pts = pts - 5
        if score!=1:
            await message.channel.send('Correct answer is: ' + info[answer] + ' meow!')
        answer = -1
    if gamePlayer!=0 and gameChannel!=0 and message.channel.id == gameChannel and message.author.id == gamePlayer and answer == -1:
        answer = random.randint(0,len(images))
        await message.channel.send('Who\'s this?')
        await message.channel.send(images[answer])
        


    

client.run('ODY0Njg3Mjg3NjE0MTc3MzIw.YO5Eyg.AAOnTnOGZi3tNk5-li4i2n3VzwY')
