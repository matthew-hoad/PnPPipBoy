# print(BrassKnuckles.name,
#     BrassKnuckles.weight,
#     BrassKnuckles.value,
#     BrassKnuckles.desc,
#     BrassKnuckles.minST,
#     BrassKnuckles.dmg,
#     BrassKnuckles.range,
#     BrassKnuckles.APS,
#     BrassKnuckles.APT,
#     BrassKnuckles.APB)
class item:
    def __init__(self,Name,Weight,Value,Description):
        self.name=Name
        self.weight=Weight
        self.value=Value
        self.desc=Description

class weapon:
    def __init__(self,Name,Value, minST,Weight,Dmg,Range,APS,APT,APB):
        self.name=Name
        self.weight=Weight
        self.value=Value
        self.minST=minST
        self.dmg=Dmg
        self.range=Range
        self.APS=APS
        self.APT=APT
        self.APB=APB
        self.itemDetails=[self.name,
        self.weight,
        self.value,
        self.minST,
        self.dmg,
        self.range,
        self.APS,
        self.APT,
        self.APB]

BrassKnuckles=weapon('Brass Knuckles',1,40,1,'1d10 + MD',1,3,4,None)
TigerClaw=weapon('Tiger Claw',70,1,1,'1d2 + MD',1,3,4,None)
Sappers=weapon('Sappers',80,3,2,'1d4 + MD',1,3,4,None)
Shredders=weapon('Shredders',90,1,2,'1d4 + MD',1,3,4,None)
Lacerators=weapon('Lacerators',100,1,2,'1d8 + 2 + MD',1,3,4,None)
MaceGlove=weapon('Mace Glove',150,3,5,'1d12 + MD',1,3,4,None)
SpikedGloves=weapon('Spiked Gloves',250,1,1,'1d10 + 4 + MD',1,3,4,None)
BoxingGloves=weapon('Boxing Gloves',250,1,2,'1d4 + MD',1,3,4,None)
PlatedBoxingGloves=weapon('Plated Boxing Gloves',300,1,5,'1d4 + 5 + MD',1,3,4,None)
PunchGun=weapon('Punch Gun',600,2,7,'1d4 + Ammo + MD',1,4,5,None)
AdamantineClaws=weapon('Adamantine Claws',1000,2,3,'1d10 + 5 + MD',1,3,4,None)
PowerFist=weapon('Power Fist',1800,1,10,'2d8 + 10 + MD',1,4,5,None)
MegaPowerFist=weapon('Mega Power Fist',2200,1,10,'3d10 + 20 + MD',1,4,5,None)
Rock=weapon('Rock',0,1,1,'1d4 + MD',1,3,4,None)
Sap=weapon('Sap',1,5,1,None,1,None,5,None)
Shiv=weapon('Shiv',2,1,1,'1d4',1,3,4,None)
SharpenedPole=weapon('Sharpened Pole',5,3,3,'1d4 + 1 + MD',2,3,4,None)
MetalPipe=weapon('Metal Pipe',10,5,10,'1d10 + MD',1,4,5,None)
WoodenClub=weapon('Wooden Club',10,3,5,'1d8 + MD',1,3,4,None)
PoliceBaton=weapon('Police Baton',30,3,3,'1d10 + MD',1,3,4,None)
Shovel=weapon('Shovel',30,5,15,'1d12 + MD',2,4,5,None)
Knife=weapon('Knife',40,2,1,'1d10 + MD',1,3,4,None)
ClawHammer=weapon('Claw Hammer',40,2,4,'1d10 + MD',1,3,4,None)
Axe=weapon('Axe',45,3,2,'1d8 + MD',1,3,4,None)
SwitchBlade=weapon('SwitchBlade',50,1,1,'1d6 + MD',1,3,4,None)
Wrench=weapon('Wrench',65,3,4,'1d6 + 2 + MD',1,4,5,None)
Crowbar=weapon('Crowbar',65,5,5,'1d12 + 3 + MD',1,4,5,None)
Spear=weapon('Spear',80,4,4,'1d12 + 3 + MD',2,4,5,None)
Machete=weapon('Machete',100,4,1,'1d10 + 7 + MD',1,4,5,None)
SledgeHammer=weapon('SledgeHammer',120,6,12,'3d4 + MD',2,4,5,None)
Scalpel=weapon('Scalpel',140,1,1,'1d8 + 3 + MD',1,3,4,None)
CombatKnife=weapon('Conbat Knife',165,2,2,'1d12 + 3 + MD',1,3,4,None)
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()
# =weapon()







# '''self,Name,Weight,Value,Description, minST,Dmg,Range,APS,APT,APB'''

#print Sappers.__class__.__name__