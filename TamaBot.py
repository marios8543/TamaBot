import discord
from discord.ext.commands import Bot
import pbot_orm
import os
import json

client = Bot(command_prefix=">")
cfg = json.loads(open("config.json","r").read())
db = pbot_orm.ORM(None,None)

for module in os.listdir(os.path.join(os.path.dirname(__file__),'modules')):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    print('Imported module {}'.format(module[:-3]))
    __import__('modules.'+module[:-3],fromlist='*')
del module

@client.event
async def on_ready():
    cnx = await pbot_orm.mysql_connect(host=cfg['dbhost'],user=cfg['dbuser'],pw=cfg['dbpass'],db=cfg['dbdb'])
    db.db = cnx[1]
    db.conn = cnx[0]
    return print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '
    +str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')