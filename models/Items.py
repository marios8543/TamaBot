als = {'hunger':'HG','cost':'TP','weight':'WG','happy':'HA'}

class Item():
    def __init__(self,name,cost,happy=0,hunger=0,weight=0):
        self.name=name
        self.code=name.replace(" ","_")
        self.cost=cost
        self.happy=happy
        self.hunger=hunger
        self.weight=weight

Meals = {
    'Kebab': Item("Kebab",180,hunger=10),
    'Beef' : Item("Beef",180,hunger=10),
    'Hamburger' : Item("Hamburger",180,hunger=10),
    'Cheese' : Item("Cheese",100,hunger=5),
    'Turkey' : Item("Turkey",600,hunger=50,happy=20),
    'Noodles' : Item("Kebab",90,hunger=5),
    'Fish' : Item("Kebab",90,hunger=5)
}

Sweets = {
    'Apple_Pie' : Item("Apple Pie",200,happy=10,weight=5),
    'Chocolate' : Item("Chocolate",150,happy=10,weight=10),
    'Cookie' : Item("Cookie",150,happy=10,weight=10),
    'Ice_Cream' : Item("Ice Cream",100,happy=10,weight=20),
    'Parfait' : Item("Parfait",150,happy=10,weight=10)
}

Snacks = {
    'Hotdog' : Item("Hotdog",250,happy=10,hunger=5,weight=10),
    'PopCorn' : Item("Popcorn",250,happy=10,hunger=5,weight=10),
    'Pizza' : Item("Pizza",250,happy=10,hunger=5,weight=10),
    'Pasta' : Item("Pasta",300,happy=20,hunger=5,weight=10),
    'Taco' : Item("Taco",250,happy=10,hunger=5,weight=10)
}

Items = {}
Items.update(Meals)
Items.update(Sweets)
Items.update(Snacks)