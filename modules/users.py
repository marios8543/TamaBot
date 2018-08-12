from TamaBot import client,db,cfg
from models import User,Items
from datetime import datetime,timedelta
import discord


@client.command(pass_context=True)
async def daily(ctx):
    usr = await User.User(ctx.message.author.id)
    if not usr:
        return await client.say(":negative_squared_cross_mark:  Not registered")
    if not usr.last_daily or (datetime.now()-usr.last_daily).seconds//3600>cfg['daily_hrs']:
        usr.credit+=cfg['daily_credits']
        usr.last_daily=datetime.now()
        await usr.update()
        await client.say(":moneybag: {}TP have just been deposited to your account".format(cfg['daily_credits']))
    else:
        tm = timedelta(hours=cfg['daily_hrs'])-(datetime.now()-usr.last_daily)
        await client.say(":negative_squared_cross_mark: You can't use this yet. Try again in {}".format(str(tm)[:-7]))
    return

@client.group(pass_context=True)
async def items(ctx):
    if not ctx.invoked_subcommand:
        usr = await User.User(ctx.message.author.id)
        if not usr:
            return await client.say(":negative_squared_cross_mark:  Not registered")
        eb = discord.Embed()
        for i,q in usr.items.items():
            v="Cost:{} | ".format(i.cost)
            for atr,val in i.__dict__.items():
                if atr in Items.als and atr!='cost':
                    v+="{}:{} | ".format(Items.als[atr],val/10)
            eb.add_field(name="{} (Qty:{})".format(i.name,q),value=v,inline=False)
        eb.set_footer(text="Do >items with any of the above to use it on your pet")
        return await client.say(":school_satchel: ***{}'s items***".format(ctx.message.author.name),embed=eb)

@items.command(pass_context=True)
async def use(ctx,arg=None):
    usr = await User.User(ctx.message.author.id)
    if not usr:
        return await client.say(":negative_squared_cross_mark:  Not registered")
    if not arg:
        return await client.say(":negative_squared_cross_mark: You haven't specified an item")
    item = Items.Items[arg]
    if usr.pet.use_item(item):
        #TODO RENDER PET WITH UPDATED PROPERTIES
        pass
    else:
        await client.say(":negative_squared_cross_mark: You don't seem to have that item. You can buy it with >shop buy")
    return

@client.command(pass_context=True)
async def profile(ctx):
    if len(ctx.message.mentions)>0:
        usr = await User.User(ctx.message.mentions[0].id)
    else:
        usr = await User.User(ctx.message.author.id)
    if not usr:
        return await client.say(":negative_squared_cross_mark:  Not registered")   
    eb = discord.Embed()
    eb.add_field(name="Pet name",value="**{}**".format(usr.pet.name))
    eb.add_field(name="Credits",value="**{}TP**".format(usr.credit))
    eb.add_field(name="Player since",value="**{}**".format(usr.registration_date))
    eb.set_footer(text="Do >pet to see your pet | Do >items to see your items")
    return await client.say(":card_index: **Profile card for __{}__**".format(str(usr.user)),embed=eb)
