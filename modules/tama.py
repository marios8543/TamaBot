from TamaBot import client,db
from models import User,Pet
from dateutil import parser
import random

@client.command(pass_context=True)
async def register(ctx):
    await client.say("Welcome to the world of Tama. Check your PMs")
    await client.send_message(ctx.message.author,"""
    ***Again welcome...it's great to have you here***
    Registering on TamaBot is easy af. Just enter your birthday below as __MM/DD/YYYY__.
    If you don't want to provide your birthday just say no although you might miss out on some birthday surprises ;)
    After that you will be assigned a pet. You will need to take good care of him.
    """)
    msg = await client.wait_for_message(author=ctx.message.author,channel=None,timeout=60)
    msg = msg.content
    bday = None
    try:
        bday = parser.parse(msg)
    except ValueError:
        pass
    gender = random.choice([0,1])
    if gender==0:
        await client.send_message(ctx.message.author,"A new Tomo has been born...and it's a boy!!! Soo how would you like to name him ?")
    else:
        await client.send_message(ctx.message.author,"A new Tomo has been born...and it's a girl!!! Soo how would you like to name her ?")
    while True:
        msg = await client.wait_for_message(author=ctx.message.author,channel=None,timeout=120)
        msg = msg.content
        if len(msg)<15:
            name = msg
            break
        else:
            await client.send_message(ctx.message.author,":negative_squared_cross_mark: Your pet's name can't be longer than 15 characters...")
    usr = await User.create_user(ctx.message.author.id,bday)
    await usr.create_pet(name,gender)
    return await client.send_message(ctx.message.author,"Whoo what a day...you got registered and got yourself a lovely little friend. Take good care of it :D")

@client.command(pass_context=True)
async def pet(ctx):
    usr = await User.User(ctx.message.author.id)
    if not usr:
        return await client.say(":negative_squared_cross_mark:  Not registered")
    pet = usr.pet
    
    

