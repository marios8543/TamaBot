from TamaBot import client,db
from models import Tamas,User

async def Pet(owner_id):
    rs = await db.select(table='pets',fields=['name','gender','hunger','happy','discipline','cycle','weight'],params={'owner':owner_id})
    if rs:
        pet = _Pet()
        pet.name = rs.name
        pet.gender = rs.gender
        pet.hunger = rs.hunger
        pet.happy = rs.happy
        pet.discipline = rs.discipline
        pet.cycle = Tamas.LifeCycle(rs.cycle)
        pet.weight = rs.weight
        pet.owner = User.User(owner_id)
        return pet

class _Pet():
    name = ""
    gender = None
    cycle = 0
    hunger=0
    happy=0
    discipline=0
    weight = 0
    owner = None

    async def update(self):
        return db.update(table='pets',values={
            "cycle":self.cycle,
            "hunger":self.hunger,
            "happy":self.happy,
            "discipline":self.discipline,
            "weight":self.weight
        },params={"owner":self.owner.id})

    async def use_item(self,item):
        if item in self.owner.items:
            if self.owner.items[item]==1:
                self.owner.items.pop(item)
            else:
                self.owner.items[item]-=1
            for atr,val in item.__dict__.items():
                if atr in self.__dict__.items() and atr!='name':
                    if getattr(self,atr)-val<50:
                        setattr(self,atr,50)
                    else:
                        setattr(self,atr,getattr(self,atr)+val)
            self.update()
            return 1

