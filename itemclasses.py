class misc:
    def __init__(self,Name,Weight,Value,Description):
        self.name=Name
        self.weight=Weight
        self.value=Value
        self.description=Description
        self.itemType='misc'

class weapon:
    def __init__(self,Name,Value, minST,Weight,Dmg,Range,APS,APT,APB,**kwargs):
        self.name=Name
        self.value=Value
        self.minST=minST
        self.weight=Weight
        self.dmg=Dmg
        self.range=Range
        self.APS=APS
        self.APT=APT
        self.APB=APB
        self.itemType='weapon'
        self.AmmoType=None
        try:
            self.ammoType=kwargs['ammoType']
        except:
            self.ammoType=None
        try:
            self.magSize=kwargs['magSize']
        except:
            self.magSize=None
        self.itemDetails=[self.name,
        self.value,
        self.minST,
        self.weight,
        self.dmg,
        self.range,
        self.APS,
        self.APT,
        self.APB,
        self.ammoType,
        self.magSize]

class apparel:
    def __init__(self,Name,Value, Weight, AC, N, L, F, P, E, ApparelType):
        self.name=Name
        self.value=Value
        self.weight=Weight
        self.AC=AC
        self.N=N
        self.L=L
        self.F=F
        self.P=P
        self.E=E
        self.ApparelType=ApparelType
        self.itemType=self.ApparelType
        self.itemDetails=[self.name,
        self.value,
        self.weight,
        self.AC,
        self.N,
        self.L,
        self.F,
        self.P,
        self.E,
        self.ApparelType]

class aid:
    def __init__(self,Name,Value,Weight,HP,Rad,Poison,ST,PE,EN,CH,IN,AG,LK,radRes,poisonRes):
        self.name=Name
        self.value=Value
        self.weight=Weight
        self.HP=HP
        self.rad=Rad
        self.poison=Poison
        self.ST=ST
        self.PE=PE
        self.EN=EN
        self.CH=CH
        self.IN=IN
        self.AG=AG
        self.LK=LK
        self.radRes=radRes
        self.poisonRes=poisonRes
        self.itemType='aid'

class ammo:
    def __init__(self, Name, Value, Weight, AC, DR):
        self.itemType='ammo'
        self.name=Name
        self.value=Value
        self.weight=Weight
        self.AC=AC
        self.DR=DR