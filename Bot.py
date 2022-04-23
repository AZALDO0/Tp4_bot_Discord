
import discord 
import logging
from CLI_ceBot import Parser
from discord.ext import commands
default_intents=discord.Intents.default()
default_intents.members= True
"""
1-Bot définition : Un bot est un programme informatique automatisé qui à les mêmes droits d'utilisateur  
que sont concepteur et qui réalise des tâches  de façon automatique en fonction de ceux pourquoi il a été programmer


2- est une façon de suivre les événements qui ont lieu durant le fonctionnement d'un logiciel. Le développeur du logiciel
 ajoute des appels à l'outil de journalisation dans son code pour indiquer que certains événements ont eu lieu. Un événement
  est décrit par un message descriptif, qui peut éventuellement contenir des données variables (c'est-à-dire qui peuvent être
   différentes pour chaque occurrence de l'événement). Un événement a aussi une importance que le développeur lui attribue ;
    cette importance peut aussi être appelée niveau ou sévérité.  

    Un log est simplement la notification d'un événement d'une importance plus ou moins élevée envoyée 
    par un service, un système, un élément réseau ou une application. 
"""
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")    
    

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        logging.warning(f"{self.user} has connected to Discord!")

class CommandBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            logging.warning('Welcome {0.mention}.'.format(member))
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):#There is the context and tne number of messages (It's the name of the method which is the command)
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            logging.warning('Hello {0.name}~'.format(member))
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member
    @commands.command()#This is the command to delete messages 
    async def delete(self, ctx,number_of_messages: int):#There is the context and tne number of messages (It's the name of the method which is the command)
        """To delete messages """
      # async def delete(ctx,number_of_messages: int):
        messages = await ctx.channel.history(limit=number_of_messages +1).flatten()
        logging.warning(f"The {number_of_messages} last messages has been deleted")
        for each_message in messages:
            
            await each_message.delete()  


args = Parser().giveArg() # Lancer le passage d'argument en ligne de commande 
fich=args.config
logFile=args.logged #Nom du fichier pour la journalisation
logging.basicConfig(

        filename=logFile,

        format='%(asctime)s -- %(message)s --',

        datefmt='%m/%d/%Y %I:%M:%S',

        encoding='utf-8',

        level=logging.WARN

    )
client = MyBot()
client.add_cog(CommandBot(client))#utiliser pour pouvoir faire la journalisation 
with open(fich, "r+") as file: #Lecture dans le fichier passer en argument de la commande qui porte le nom du ficher du token 
    rFile=file.readline()
    token=str(rFile) 
    file.close()
    
client.run(token)#Mettant le token depuis le mode dévelopeur sur le navigateur  



