from TamaBot import db,client
from models import Items,User
import asyncio
import discord


@client.group(pass_context=True)
async def shop(ctx):
    if not ctx.invoked_subcommand:
        usr = await User.User(ctx.message.author.id)
        if not usr:
            return await client.say(":negative_squared_cross_mark:  Not registered")
        home = await client.say("""
        :shopping_cart: ***What would you like to buy ?***
        :regional_indicator_a: __Meals__
        :regional_indicator_b: __Sweets__
        :regional_indicator_c: __Snacks__
        :regional_indicator_d: __Toys__
        """)
        await client.add_reaction(home,"\U0001f1e6")
        await client.add_reaction(home,"\U0001f1e7")
        await client.add_reaction(home,"\U0001f1e8")
        rhome = await client.wait_for_reaction(user=ctx.message.author,message=home)
        if rhome.reaction.emoji=="\U0001f1e6":
            eb=discord.Embed()
            eb.set_author(name="Meal Shop")
            for n,m in Items.Meals.items():
                if m in usr.items:
                    inv = usr.items[m]
                else:
                    inv=0    
                eb.add_field(name=m.name,value="Cost: {}TP (+{}HG). You currently have {}".format(m.cost,m.hunger/10,inv))
        elif rhome.reaction.emoji=="\U0001f1e7":
            eb=discord.Embed()
            eb.set_author(name="Sweet Shop")
            for n,m in Items.Sweets.items():
                if m in usr.items:
                    inv = usr.items[m]
                else:
                    inv=0
                eb.add_field(name=m.name,value="Cost: {}TP (+{}HA, +{}WG). You currently have {}".format(m.cost,m.happy/10,m.weight/10,inv))
        elif rhome.reaction.emoji=="\U0001f1e8":
            eb=discord.Embed()
            eb.set_author(name="Snack Shop")
            for n,m in Items.Snacks.items():
                if m in usr.items:
                    inv = usr.items[m]
                else:
                    inv=0
                eb.add_field(name=m.name,value="Cost: {}TP (+{}HA, +{}HG, +{}WG). You currently have {}".format(m.cost,m.happy/10,m.hunger/10,m.weight/10,inv))
        else:
            eb=discord.Embed(title="Not implemented")
        eb.set_footer(text="Type >>shop buy and the name of the item you want to buy")
        await client.delete_message(home)
        return await client.say(embed=eb)

@shop.command(pass_context=True)
async def buy(ctx,*args):
    usr = await User.User(ctx.message.author.id)
    if not usr:
        return await client.say(":negative_squared_cross_mark:  Not registered")
    if " ".join(args).replace(" ","_") in Items.Items:
        item = Items.Items[" ".join(args).replace(" ","_")]
        if usr.credit>=item.cost:
            eb = discord.Embed(title="Are you sure you want to buy this item ?")
            eb.add_field(name="Item: __***{}***__  -  Price: **{}TP**".format(item.name,item.cost),value="After this purchase you will have **{}TP** left".format(usr.credit-item.cost))
            eb.set_footer(text="You currently have {}TP".format(usr.credit))
            msg = await client.say(embed=eb)
            await client.add_reaction(msg,"\U0001f44d")
            await client.add_reaction(msg,"\U0001f44e")
            rmsg = await client.wait_for_reaction(message=msg,user=ctx.message.author)
            if rmsg.reaction.emoji=="\U0001f44d":
                if await usr.buy(item):
                    await client.say(":white_check_mark: Purchase successful. Thanks for stopping by!")
                else:
                    await client.say(":negative_squared_cross_mark: Something went wrong. Are you sure you have enough credit ?")
            else:
                await client.say(":zzz: See ya next time!")
            return await client.delete_message(msg)
        else:
            return await client.say(":negative_squared_cross_mark: You don't have enough credit to make this purchase. You need an additional {}TP".format(item.cost-usr.credit)) 
    else:
        return await client.say(":negative_squared_cross_mark: Hmm I can't seem to find that item. Are you sure you typed it correctly ?")


    