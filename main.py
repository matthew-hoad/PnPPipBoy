from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.listview import ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.graphics import Color
from kivy.factory import Factory
from math import floor
import os
import random as r

Builder.load_string("""
<PipLabel>:
  bcolor: 0, 0.8, 0, 0.4
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

class misc:
    def __init__(self,Name,Weight,Value,Description):
        self.name=Name
        self.weight=Weight
        self.value=Value
        self.desc=Description

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
        try:
            self.AmmoType=kwargs['AmmoType']
        except:
            self.AmmoType=None
        self.itemDetails=[self.name,
        self.value,
        self.minST,
        self.weight,
        self.dmg,
        self.range,
        self.APS,
        self.APT,
        self.APB,
        self.AmmmoType]

class apparel:
    def __init__(self,Name,Value, Weight, Ac, N, L, F, P, E, ApparelType):
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

class PlayerTrait:
    def __init__(self,name,desc):
        self.name=name
        self.desc=desc

class PipLabel(Label):
    def __init__(self, **kwargs):
        super(PipLabel, self).__init__(**kwargs)
        #self.canvas.add(Color(0,0.5,0,0.5))
        bcolor = ListProperty([1,1,1,1])

class PipLabel2(PipLabel):
    def __init__(self, **kwargs):
        super(PipLabel, self).__init__(**kwargs)
        #self.canvas.add(Color(0,0.5,0,0.5))
        bcolor = ListProperty([1,1,1,1])
        self.size=self.texture_size

class PipButton(Button):
    def __init__(self, **kwargs):
        super(PipButton, self).__init__(**kwargs)
        self.background_normal=''
        self.background_color=(0,0.8,0,0.4)

class RemoveItemButton(PipButton):
    def __init__(self, **kwargs):
        super(RemoveItemButton, self).__init__(**kwargs)
        self.background_normal=''
        self.background_color=(0.8,0,0,0.4)

class PipToggleButton(ToggleButton):
    def __init__(self, **kwargs):
        super(PipToggleButton, self).__init__(**kwargs)
        self.background_normal=''
        self.background_color=(0,0.8,0,0.4)
        self.purpose=kwargs['purpose']
    def updateEquippedWeapon(self,root):
        pass

    def updateSelectedTraits(self,root):
        #print self.state
        if self.state=='down':
            import traits as t
            for trait in t.AvailableTraits:
                #print self.text,' = ',trait.name
                if self.text==trait.name:
                    if root.playerCharacter.traits.count([trait.name,trait.desc])==0:
                        root.playerCharacter.traits.append([trait.name,trait.desc])
                    else:
                        pass
                    #print root.playerCharacter.traits
        elif self.state=='normal':
            import traits as t
            for trait in t.AvailableTraits:
                #print self.text,' = ',trait.name
                if self.text==trait.name:
                    try:
                        root.playerCharacter.traits.remove([trait.name,trait.desc])
                    except:
                        pass
                    #print root.playerCharacter.traits

    def updateAll(self,root):
        if self.purpose=='traits':
            self.updateSelectedTraits(root)

Factory.register('KivyB', module='PipLabel')

class character:
    def __init__(self,SPECIAL,characterDetails,Traits,inventory,EXP):
        self.special=SPECIAL
        self.characterDetails=characterDetails
        self.traits=Traits
        self.inventory=inventory
        self.EXP=EXP
        self.ST=self.special[0]
        self.PE=self.special[1]
        self.EN=self.special[2]
        self.CH=self.special[3]
        self.IN=self.special[4]
        self.AG=self.special[5]
        self.LK=self.special[6]
        self.maxHP=int(15 + (self.ST + (2*self.EN)))
        self.level = self.checkLevel()
        self.HP=int(self.maxHP)
        self.poison = 0
        self.rads = 0

        self.poisonandrads=[self.poison,self.rads]

        self.smallGuns=5+4*self.AG
        self.bigGuns=0+2*self.AG
        self.energyWeapons=0+2*self.AG
        self.unarmed=30+2*(self.AG+self.ST)
        self.meleeWeapons=20+2*(self.AG+self.ST)
        self.throwing=0+4*self.AG
        self.firstAid=2*(self.PE+self.IN)
        self.doctor=5+(self.PE+self.IN)
        self.sneak=5+3*self.AG
        self.lockpick=10 + (self.PE+self.AG)
        self.steal=0 + 3*self.AG
        self.traps=0+ (self.PE+self.AG)
        self.science=0+(4*self.IN)
        self.repair=0+3*self.IN
        self.pilot=0+2*(self.AG+self.PE)
        self.speech=0+5*self.CH
        self.barter=0+4*self.CH
        self.gambling=0+5*self.LK
        self.outdoorsman=0+2*(self.EN+self.IN)

        self.AP=5+floor(self.AG/2.0)
        self.carryWeight=(25+25*self.ST)
        self.meleeDamage=[self.ST-5 if self.ST-5>0 else 1]
        self.poisonRes=5*self.EN
        self.radRes=2*self.EN
        self.sequence=2*self.PE
        self.healingRate=floor(self.EN/3.0)
        self.criticalChance=self.LK
        self.electricityres=0
        self.gasres=0
        self.implantendurance=(10*(self.IN+self.EN))
        
        self.secondaryStats=[self.AP,self.carryWeight,self.meleeDamage,self.poison,self.radRes,self.sequence,self.healingRate,self.criticalChance,self.electricityres,self.gasres,self.implantendurance]

        self.skills=[self.smallGuns,self.bigGuns,self.energyWeapons,self.unarmed,self.meleeWeapons,self.throwing,self.firstAid,self.doctor,self.sneak,self.lockpick,self.steal,self.traps,self.science,self.repair,self.pilot,self.speech,self.barter,self.gambling,self.outdoorsman]

        self.currentlyEquipped={'weapon':None,'head':None,'body':None,'aid':None}

        self.update()

    def addItem(self,item):
        with open('items.py','a') as itemsfile:
            preparedString='{} = {}('.format(item.name.replace(' ',''),item.__class.__name__)
            if item.__class__.__name__ == 'weapon':
                preparedString+="'{}',{},{},{},'{}',{},{},{},{}".format(item.name,item.value,item.nimST,item.weight,item.dmg, item.range,item.APS,item.APT,item.APB)
            elif item.__class__.__name__ == 'apparel':
                preparedString+="'{}',{},{},'{}','{}','{}','{}','{}','{}','{}'".format(item.name,item.value,item.weight,item.AC, item.N,item.L,item.F,item.P,item.E,item.ApparelType)
            itemsfile.write(preparedString)
        self.inventory.append

    def equipItem(self,item):
        self.currentlyEquipped['{}'.format(item.itemType)]=item
        #print str(item),'should be equipped now'

    def removeItem(self,itemtoberemoved):
        try:
            counter=0
            for item in self.inventory:
                if counter==0 and item.name==itemtoberemoved.name:
                    counter+=1
                    #print self.inventory
                    self.inventory.remove(itemtoberemoved)
                    #print self.inventory
        except:
            pass

    def addEXP(self, exp):
        self.EXP+=exp
        checkLevel()

    def checkLevel(self):
        if self.EXP>=0 and self.EXP<1000:
            self.level=1
        elif self.EXP>=1000 and self.EXP<3000:
            self.level=2
        elif self.EXP>=3000 and self.EXP<6000:
            self.level=3
        elif self.EXP>=6000 and self.EXP<10000:
            self.level=4
        elif self.EXP>=10000 and self.EXP<15000:
            self.level=5
        elif self.EXP>=15000 and self.EXP<21000:
            self.level=6
        elif self.EXP>=21000 and self.EXP<28000:
            self.level=7
        elif self.EXP>=28000 and self.EXP<36000:
            self.level=8
        elif self.EXP>=36000 and self.EXP<45000:
            self.level=9
        elif self.EXP>=45000 and self.EXP<55000:
            self.level=10
        elif self.EXP>=55000 and self.EXP<66000:
            self.level=11
        elif self.EXP>=66000 and self.EXP<78000:
            self.level=12
        elif self.EXP>=78000 and self.EXP<91000:
            self.level=13
        elif self.EXP>=91000 and self.EXP<105000:
            self.level=14
        self.maxHP+=int((3+floor(self.EN/2.0))*self.level)
        return self.level

    def update(self):
        #print 'Updating Character'

        #print self.currentlyEquipped
        #print self.inventory

        if self.poison<0:
            self.poison=0
        if self.rads<0:
            self.rads=0

        self.name=self.characterDetails[0]
        self.gender=self.characterDetails[1]
        self.race=self.characterDetails[2]
        self.age=self.characterDetails[3]
        self.karma=self.characterDetails[4]
        self.notes=self.characterDetails[5]


        self.ST=self.special[0]
        self.PE=self.special[1]
        self.EN=self.special[2]
        self.CH=self.special[3]
        self.IN=self.special[4]
        self.AG=self.special[5]
        self.LK=self.special[6]

        if self.race == 'Human':
            self.SPECIALpoints=40
        elif self.race == 'Super Mutant':
            self.SPECIALpoints=40
        elif self.race == 'Ghoul':
            self.SPECIALpoints=42
        else:
            self.SPECIALpoints=40
        self.SPECIALpoints-=int(self.ST)+int(self.PE)+int(self.EN)+int(self.CH)+int(self.IN)+int(self.AG)+int(self.LK)

        self.maxHP=int(15 + (self.ST + (2*self.EN)))
        self.level = self.checkLevel()

        if self.HP>self.maxHP:
            self.HP=int(self.maxHP)

        self.currentEncumbrance=0
        for item in self.inventory:
            self.currentEncumbrance+=int(item.weight)
        
        
        self.AP=self.secondaryStats[0]
        self.carryWeight=self.secondaryStats[1]
        self.meleeDamage=self.secondaryStats[2]
        self.poisonRes=self.secondaryStats[3]
        self.radRes=self.secondaryStats[4]
        self.sequence=self.secondaryStats[5]
        self.healingRate=self.secondaryStats[6]
        self.criticalChance=self.secondaryStats[7]
        self.electricityres=self.secondaryStats[8]
        self.gasres=self.secondaryStats[9]
        self.implantendurance=self.secondaryStats[10]

        
        self.smallGuns=self.skills[0]
        self.bigGuns=self.skills[1]
        self.energyWeapons=self.skills[2]
        self.unarmed=self.skills[3]
        self.meleeWeapons=self.skills[4]
        self.throwing=self.skills[5]
        self.firstAid=self.skills[6]
        self.doctor=self.skills[7]
        self.sneak=self.skills[8]
        self.lockpick=self.skills[9]
        self.steal=self.skills[10]
        self.traps=self.skills[11]
        self.science=self.skills[12]
        self.repair=self.skills[13]
        self.pilot=self.skills[14]
        self.speech=self.skills[15]
        self.barter=self.skills[16]
        self.gambling=self.skills[17]
        self.outdoorsman=self.skills[18]


        for trait in self.traits:
            if trait[0]=='Bruiser':
                self.ST+=2
            elif trait[0]=='Gifted':
                self.ST+=1
                self.PE+=1
                self.EN+=1
                self.CH+=1
                self.IN+=1
                self.AG+=1
                self.LK+=1

        self.poisonandrads=[self.poison,self.rads]

        self.secondaryStats=[self.AP,self.carryWeight,self.meleeDamage,self.poison,self.radRes,self.sequence,self.healingRate,self.criticalChance,self.electricityres,self.gasres,self.implantendurance]

        self.skills=[self.smallGuns,self.bigGuns,self.energyWeapons,self.unarmed,self.meleeWeapons,self.throwing,self.firstAid,self.doctor,self.sneak,self.lockpick,self.steal,self.traps,self.science,self.repair,self.pilot,self.speech,self.barter,self.gambling,self.outdoorsman]
        #print 'Finished Updating Character'

class DataItem(object):
    def __init__(self, text='', is_selected=False):
        self.text = text
        self.is_selected = is_selected

class dummyDataItem(object):
    def __init__(self, text='', is_selected=False):
        self.text = text
        self.is_selected = False

import charac

player=character(SPECIAL=charac.SPECIAL,characterDetails=charac.characterDetails,Traits=charac.traits,inventory=charac.inventory,EXP=charac.EXP)
try:
    player.poison=charac.poisonandrads[0]
    player.rads=charac.poisonandrads[1]
    player.skills=charac.skills
    player.HP=charac.HP
    print 'HP updated'
except:
    pass
player.update()
presentation=Builder.load_file('main.kv')

class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
    playerCharacter=player

    def updateTraitsAndWeapons(self,root):
        for childs in root.ids.PlayerTraits.children:
            for child in childs.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton':
                    #print 'Found one!'
                    child.updateAll(root)


    def setEquipped(self,inv):
        foundAnEquippable=False
        for row in inv.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton':
                    if child.state=='down' and foundAnEquippable==False:
                        #print 'Got it'
                        self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]=row.boundItem
                        self.playerCharacter.equipItem(row.boundItem)
                        foundAnEquippable=True
                    elif child.state=='normal' and foundAnEquippable==False:
                        self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]=None

    def addToInventory(self,inv):
        foundAnAddable=False
        for row in inv.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton':
                    if child.state=='down' and foundAnAddable==False:
                        #print 'Got it'
                        self.playerCharacter.inventory.append(row.boundItem)
                        foundAnAddable=True

    # def reloadCharacter(self):
    #     import charac
    #     pSPECIAL=charac.SPECIAL
    #     pcharacterDetails=charac.characterDetails
    #     ptraits=charac.traits
    #     pinventory=charac.inventory
    #     pEXP=charac.EXP
    #     player=character(SPECIAL=pSPECIAL,characterDetails=pcharacterDetails,Traits=ptraits,inventory=pinventory,EXP=pEXP)
    #     return player

    def saveCharacter(self):################### EDIT THIS TO JUST TAKE IT ALL FROM THE SELF.PLAYER OBJECT DIRECTLY
        with open('charac.py','w') as savechar:
            #print 'Saving Character'
            preparedString="import items as i\nSPECIAL=["
            preparedString+=str(self.playerCharacter.special[0])
            preparedString+=','
            preparedString+=str(self.playerCharacter.special[1])
            preparedString+=','
            preparedString+=str(self.playerCharacter.special[2])
            preparedString+=','
            preparedString+=str(self.playerCharacter.special[3])
            preparedString+=','
            preparedString+=str(self.playerCharacter.special[4])
            preparedString+=','
            preparedString+=str(self.playerCharacter.special[5])
            preparedString+=','
            preparedString+=str(self.playerCharacter.special[6])
            preparedString+=']\ncharacterDetails=["'
            preparedString+=str(self.playerCharacter.name)
            preparedString+='","'
            preparedString+=str(self.playerCharacter.gender)
            preparedString+='","'
            preparedString+=str(self.playerCharacter.race)
            preparedString+='","'
            preparedString+=str(self.playerCharacter.age)
            preparedString+='","'
            preparedString+=str(self.playerCharacter.karma)
            preparedString+='","'
            preparedString+=str(self.playerCharacter.notes)
            preparedString+='"]\ntraits=['
            for trait in self.playerCharacter.traits:
                preparedString+="['"+trait[0]+"','''"+trait[1]+"'''],"
            if preparedString[-1]==',':
                preparedString=preparedString[:-1]
            preparedString+=']\ninventory=['
            for item in self.playerCharacter.inventory:
                #print item
                preparedString+='i.'+item.name.replace(' ','')+','
            if preparedString[-1]==',':
                preparedString=preparedString[:-1]
            preparedString+="]\nEXP={}".format(str(self.playerCharacter.EXP))
            preparedString+="\npoisonandrads=[{},{}]".format(self.playerCharacter.poison,self.playerCharacter.rads)
            listofskillnames=['smallGuns', 'bigGuns', 'energyWeapons', 'unarmed', 'meleeWeapons', 'throwing', 'firstAid', 'doctor', 'sneak', 'lockpick', 'steal', 'traps', 'science', 'repair', 'pilot', 'speech', 'barter', 'gambling', 'outdoorsman',]
            for i in range(len(self.playerCharacter.skills)):
                preparedString+="\n{}={}".format(listofskillnames[i],self.playerCharacter.skills[i])
            preparedString+="\nskills=["
            for skillname in listofskillnames:
                preparedString+=skillname+','
            if preparedString[-1]==',':
                preparedString=preparedString[:-1]
            preparedString+=']'
            preparedString+="\nHP={}".format(self.playerCharacter.HP)
            savechar.write(preparedString)


class SpecialLabel(PipLabel):
    def __init__(self, **kwargs):
        super(SpecialLabel, self).__init__(**kwargs)
    def updateLabel(self,root, XX, i):
        self.text='{}: {}'.format(XX, root.playerCharacter.special[i])

class CharDetailLabel(PipLabel):
    def __init__(self, **kwargs):
        super(CharDetailLabel, self).__init__(**kwargs)
    def updateLabel(self,root,idString,proprty):
        if idString == 'HP':
            self.text = 'HP: {}/{}'.format(root.playerCharacter.HP,root.playerCharacter.maxHP)
        elif idString=='Name':
            self.text='{}: {}'.format(idString,proprty)
        elif idString=='CarryWeight':
            self.text='CarryWeight: {}/{}'.format(root.playerCharacter.currentEncumbrance,root.playerCharacter.carryWeight)
        else:
            self.text='{}: {}'.format(str(idString), proprty)

class StatLabel(PipLabel):
    def __init__(self, **kwargs):
        super(StatLabel, self).__init__(**kwargs)
        self.background_normal=''
        self.background_color=(0.1,0.1,0.1,1)

class SPECIALrow(BoxLayout):
    def __init__(self, **kwargs):
        super(SPECIALrow, self).__init__(**kwargs)
        self.padding=(5,5)
        self.spacing=5

class characterDetailsInput(TextInput):
    def __init__(self, **kwargs):
        super(characterDetailsInput, self).__init__(**kwargs)
    def getText(self,root,i):
        text=root.playerCharacter.characterDetails[i]
        return str(text)
    def updateText(self,root,i):
        root.playerCharacter.characterDetails[i]=self.text
        root.playerCharacter.update()

class numLabel(PipLabel):
    def __init__(self, **kwargs):
        super(numLabel, self).__init__(**kwargs)
    value = NumericProperty(1)

    def incrment(self,root,num):
        if int(self.text)==1 and num<0:
            self.text='1'
        elif root.playerCharacter.SPECIALpoints==0 and num<0:
            self.text=str(int(self.text)+num)
            root.playerCharacter.SPECIALpoints-=num
        elif int(self.text)==10 and num<0:
            self.text=str(int(self.text)+num)
            root.playerCharacter.SPECIALpoints-=num
        elif root.playerCharacter.SPECIALpoints!=0 and int(self.text)<10:
            self.text=str(int(self.text)+num)
            root.playerCharacter.SPECIALpoints-=num

    def getNum(self,root,i):
        text=root.playerCharacter.special[i]
        return str(text)

    def updateNum(self,root,i):
        root.playerCharacter.special[i]=int(self.text)
        root.playerCharacter.update()

class SkillLabel(PipLabel):
    def __init__(self, **kwargs):
        super(SkillLabel, self).__init__(**kwargs)
        self.height=50
    def updateLabel(self,idString,proprty):
        self.text='{}: {}'.format(idString,proprty)

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

class ItemRow(BoxLayout):
    def __init__(self, **kwargs):
        super(ItemRow, self).__init__(**kwargs)
        self.boundItem=kwargs['boundItem']

class PreDefinedWeaponInventory(GridLayout):
    def __init__(self, **kwargs):
        super(PreDefinedWeaponInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def search(self,text,root):
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        import items as i
        for item in i.weapons:
            if item.__class__.__name__ == 'weapon' and item.name[:len(text)].lower()==text.lower():
                WeaponRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                WeaponRow.add_widget(PipToggleButton(purpose='weapon',text=item.name,height=100,size_hint_x=0.2,group='weapon'))#,on_press=root.playerCharacter.equipItem(item)))
                Values=GridLayout(height=100,size_hint_x=0.8,cols=8,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text='minST',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text='Dmg',height=50,width=root.width*0.14))
                Values.add_widget(PipLabel(text='Rng',height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text='APS',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text='APT',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text='APB',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text=str(item.minST),height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.dmg),height=50,width=root.width*0.14))
                Values.add_widget(PipLabel(text=str(item.range),height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text=str(item.APS),height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.APT),height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.APB),height=50,width=root.width*0.09))
                WeaponRow.add_widget(Values)
                self.add_widget(WeaponRow)
        self.bind(minimum_height=self.setter('height'))

class PreDefinedApparelInventory(GridLayout):
    def __init__(self, **kwargs):
        super(PreDefinedApparelInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def search(self,text,root):
        import items as i
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in i.apparels:
            if item.__class__.__name__ == 'apparel' and item.name[:len(text)].lower() == text.lower():
                if item.ApparelType=='head':
                    #self.add_widget(PipLabel(text='Head',halign='left',size_hint_x=1,height=50,width=root.width))
                    ApparelRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='head'))#,on_press=root.playerCharacter.equipItem(item)))
                    Values=GridLayout(height=100,size_hint_x=0.7,cols=8,rows=2)
                    Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='AC',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='N',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='L',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='F',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='P',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='E',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.AC),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.N),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.L),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.F),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.P),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.E),height=50,width=root.width*0.1))
                    ApparelRow.add_widget(Values)
                    self.add_widget(ApparelRow)
                if item.ApparelType=='body':
                    #self.add_widget(PipLabel(text='Body',halign='left',size_hint_x=1,height=100))
                    ApparelRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='body'))#,on_press=root.playerCharacter.equipItem(item)))
                    Values=GridLayout(height=100,size_hint_x=0.7,cols=8,rows=2)
                    Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='AC',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='N',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='L',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='F',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='P',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='E',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.AC),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.N),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.L),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.F),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.P),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.E),height=50,width=root.width*0.1))
                    ApparelRow.add_widget(Values)
                    self.add_widget(ApparelRow)

        self.bind(minimum_height=self.setter('height'))

class PreDefinedAidInventory(GridLayout):
    def __init__(self, **kwargs):
        super(PreDefinedAidInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def search(self,text,root):
        import items as i
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in i.aids:
            if item.__class__.__name__ == 'aid' and item.name[:len(text)].lower() == text.lower():
                #print item
                AidRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AidRow.add_widget(PipToggleButton(purpose='aid',text=item.name,height=100,size_hint_x=0.2,group='aid',))#on_release=))#,on_press=root.playerCharacter.equipItem(item)))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=12,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='HP',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Rad',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Poison',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='ST',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='PE',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='EN',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='CH',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='IN',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='AG',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='LK',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.HP),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.rad),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.poison),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.ST),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.PE),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.EN),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.CH),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.IN),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.AG),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.LK),height=50,width=root.width*0.083))
                AidRow.add_widget(Values)
                self.add_widget(AidRow)
        self.bind(minimum_height=self.setter('height'))

class PreDefinedMiscInventory(GridLayout):
    def __init__(self, **kwargs):
        super(PreDefinedMiscInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def search(self,text,root):
        import items as i
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in i.miscs:
            if item.__class__.__name__ == 'misc' and item.name[:len(text)].lower() == text.lower():
                #print item
                AidRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AidRow.add_widget(PipToggleButton(purpose='misc',text=item.name,height=100,size_hint_x=0.2,group='misc',))#on_release=))#,on_press=root.playerCharacter.equipItem(item)))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=12,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                AidRow.add_widget(Values)
                self.add_widget(AidRow)
                '''Value,Weight,HP,Rad,Poison,ST,PE,EN,CH,IN,AG,LK,radRes,poisonRes'''
        self.bind(minimum_height=self.setter('height'))

class WeaponInventory(GridLayout):
    def __init__(self, **kwargs):
        super(WeaponInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'weapon':
                WeaponRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                WeaponRow.add_widget(PipToggleButton(purpose='weapon',text=item.name,height=100,size_hint_x=0.2,group='weapon'))#,on_press=root.playerCharacter.equipItem(item)))
                Values=GridLayout(height=100,size_hint_x=0.8,cols=8,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text='minST',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text='Dmg',height=50,width=root.width*0.14))
                Values.add_widget(PipLabel(text='Rng',height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text='APS',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text='APT',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text='APB',height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text=str(item.minST),height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.dmg),height=50,width=root.width*0.14))
                Values.add_widget(PipLabel(text=str(item.range),height=50,width=root.width*0.1))
                Values.add_widget(PipLabel(text=str(item.APS),height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.APT),height=50,width=root.width*0.09))
                Values.add_widget(PipLabel(text=str(item.APB),height=50,width=root.width*0.09))
                WeaponRow.add_widget(Values)
                self.add_widget(WeaponRow)
        self.bind(minimum_height=self.setter('height'))

class ApparelInventory(GridLayout):
    def __init__(self, **kwargs):
        super(ApparelInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'apparel':
                if item.ApparelType=='head':
                    #self.add_widget(PipLabel(text='Head',halign='left',size_hint_x=1,height=50,width=root.width))
                    ApparelRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='head'))#,on_press=root.playerCharacter.equipItem(item)))
                    Values=GridLayout(height=100,size_hint_x=0.7,cols=8,rows=2)
                    Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='AC',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='N',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='L',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='F',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='P',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='E',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.AC),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.N),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.L),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.F),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.P),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.E),height=50,width=root.width*0.1))
                    ApparelRow.add_widget(Values)
                    self.add_widget(ApparelRow)
                if item.ApparelType=='body':
                    #self.add_widget(PipLabel(text='Body',halign='left',size_hint_x=1,height=100))
                    ApparelRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='body'))#,on_press=root.playerCharacter.equipItem(item)))
                    Values=GridLayout(height=100,size_hint_x=0.7,cols=8,rows=2)
                    Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='AC',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='N',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='L',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='F',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='P',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text='E',height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.AC),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.N),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.L),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.F),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.P),height=50,width=root.width*0.1))
                    Values.add_widget(PipLabel(text=str(item.E),height=50,width=root.width*0.1))
                    ApparelRow.add_widget(Values)
                    self.add_widget(ApparelRow)

        self.bind(minimum_height=self.setter('height'))

class AidInventory(GridLayout):
    def __init__(self, **kwargs):
        super(AidInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'aid':
                #print item
                AidRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AidRow.add_widget(PipToggleButton(purpose='aid',text=item.name,height=100,size_hint_x=0.2,group='aid',))#on_release=))#,on_press=root.playerCharacter.equipItem(item)))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=12,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='HP',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Rad',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Poison',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='ST',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='PE',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='EN',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='CH',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='IN',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='AG',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='LK',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.HP),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.rad),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.poison),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.ST),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.PE),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.EN),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.CH),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.IN),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.AG),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.LK),height=50,width=root.width*0.083))
                AidRow.add_widget(Values)
                self.add_widget(AidRow)
        self.bind(minimum_height=self.setter('height'))

class MiscInventory(GridLayout):
    def __init__(self, **kwargs):
        super(MiscInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'misc':
                #print item
                AidRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AidRow.add_widget(PipToggleButton(purpose='misc',text=item.name,height=100,size_hint_x=0.2,group='misc',))#on_release=))#,on_press=root.playerCharacter.equipItem(item)))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=12,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                AidRow.add_widget(Values)
                self.add_widget(AidRow)
                '''Value,Weight,HP,Rad,Poison,ST,PE,EN,CH,IN,AG,LK,radRes,poisonRes'''
        self.bind(minimum_height=self.setter('height'))

class PlayerTraits(GridLayout):
    def __init__(self, **kwargs):
        super(PlayerTraits, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None
    def populate(self,root):
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        import traits as t
        for trait in t.AvailableTraits:
            TraitContainer=BoxLayout(height=400,size_hint_y=None,spacing=5)
            TraitContainer.add_widget(PipToggleButton(purpose='traits',text=trait.name))
            TraitContainer.add_widget(PipLabel2(text=trait.desc))
            self.add_widget(TraitContainer)
            #print trait.name
            #print trait.desc
            
        self.bind(minimum_height=self.setter('height'))

class PipBoy(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PipBoy().run()
