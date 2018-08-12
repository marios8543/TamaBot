from TamaBot import client,db
import models
from models import Pet,Items
import json

async def create_user(id,bday):
    await db.insert(table='users',values={
        "id":id,
        "birthday":bday
    })
    usr = _User()
    usr.id = id
    usr.birthday = bday
    usr.user = client.get_user_info(id)
    return usr

async def User(id):
    rs = await db.select(table='users',fields=['items','credit','registration_date','birthday','last_daily'],params={'id':id})
    if rs:
        usr = _User()
        usr.id = id
        usr.registration_date = rs.registration_date
        usr.birthday = rs.birthday
        if not rs.items:
            itm={}
        else:
            itm = json.loads(rs.items)
        for i,q in itm.items():
            usr.items[Items.Items[i]]=q
        if not rs.credit:
            usr.credit=0
        else:
            usr.credit = int(rs.credit)
        if not rs.last_daily:
            usr.last_daily=None
        else:
            usr.last_daily=rs.last_daily
        usr.user = await client.get_user_info(id)
        usr.pet = await Pet.Pet(id)
        return usr 

class _User():
    id = ""
    items = {}
    credit = 2500
    pet = None

    async def update(self):
        itm ={}
        for i,q in self.items.items():
            itm[i.code]=q
        itm = json.dumps(itm)
        return await db.update(table='users',values={'credit':self.credit,'last_daily':self.last_daily,'items':itm},params={'id':self.id})

    async def buy(self,item):
        if self.credit>=item.cost:
            self.credit-=item.cost
            if item in self.items:
                self.items[item]+=1
            else:
                self.items[item]=1
            await self.update()    
            return 1

    async def create_pet(self,name,gender):
        if self.pet:
            return
        await db.insert(table='pets',values={
            "owner":self.id,
            "name":name,
            "gender":gender
        })
        return await Pet.Pet(self.id)