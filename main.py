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
from kivy.uix.listview import ListItemButton
from kivy.uix.listview import ListView
from kivy.adapters.listadapter import ListAdapter
from math import floor
import os

class character:
    def __init__(self,SPECIAL,characterDetails,perks,inventory,EXP):
        self.characterDetails=characterDetails
        self.name=self.characterDetails[0]
        self.gender=self.characterDetails[1]
        self.race=self.characterDetails[2]
        self.age=self.characterDetails[3]
        self.karma=self.characterDetails[4]
        self.notes=self.characterDetails[5]

        if self.race == 'Human':
            self.SPECIALpoints=40
        elif self.race == 'Super Mutant':
            self.SPECIALpoints=40
        elif self.race == 'Ghoul':
            self.SPECIALpoints=42
        else:
            self.SPECIALpoints=40


        self.exp = EXP
        self.level = 1
        self.poison = 0
        self.rads = 0
        self.special=SPECIAL
        self.ST=self.special[0]
        self.PE=self.special[1]
        self.EN=self.special[2]
        self.CH=self.special[3]
        self.IN=self.special[4]
        self.AG=self.special[5]
        self.LK=self.special[6]

        self.SPECIALpoints-=int(self.ST)+int(self.PE)+int(self.EN)+int(self.CH)+int(self.IN)+int(self.AG)+int(self.LK)

        self.maxHP=15 + (self.ST + (2*self.EN))
        self.HP=self.maxHP
        self.AP=5+floor(self.AG/2.0)
        self.carryWeight=(25+25*self.ST)
        self.meleeDamage=[self.ST-5 if self.ST-5>0 else 1]
        self.poisonRes=5*self.EN
        self.radRes=2*self.EN
        self.sequence=2*self.PE
        self.healingRate=floor(self.EN/3.0)
        self.criticalChance=self.LK

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

        self.perks=perks

        self.inventory=inventory

    def addEXP(self, exp):
        self.EXP+=exp
        checkLevel()

    def checkLevel(self):
        oldlevel=self.level
        if self.EXP>0 and self.EXP<1000:
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
        if self.level==oldlevel+1:
            self.maxHP+= 3+floor(self.EN/2.0)
        return self.level

    def updateSPECIALAndcharacterDetails(self):
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
        self.name=self.characterDetails[0]
        self.gender=self.characterDetails[1]
        self.race=self.characterDetails[2]
        self.age=self.characterDetails[3]
        self.karma=self.characterDetails[4]
        self.notes=self.characterDetails[5]
    def normaliseItemNames(self):
        for item in self.inventory:
            if (len(item.name)%2)!=0:
                item.name+=' '

class DataItem(object):
    def __init__(self, text='', is_selected=False):
        self.text = text
        self.is_selected = is_selected

class dummyDataItem(object):
    def __init__(self, text='', is_selected=False):
        self.text = text
        self.is_selected = False

class Inventory(ListView):
    def __init__(self, **kwargs):
        super(Inventory, self).__init__(**kwargs)

    def populateItems(self,root):
        data_items = []



        for item in root.playerCharacter.inventory:
            itemDescString=''
            itemDescString+='{:<15}'.format(item.name)
            for i in range(1,len(item.itemDetails)):
                itemDescString+='{:>10}'.format(item.itemDetails[i])
            data_items.append(DataItem(text=itemDescString))
            print len(itemDescString)
        data_items.append(dummyDataItem())
        data_items.append(dummyDataItem())
        data_items.append(dummyDataItem())

        list_item_args_converter = lambda row_index, obj: {'text': obj.text,
                                                           'size_hint_y': None,
                                                           'height': 75,
                                                           'selected_color':[0,0.5,0,0.4],
                                                           'deselected_color':[0,0.5,0,0.2]
                                                           }

        list_adapter = ListAdapter(data=data_items,
                                   args_converter=list_item_args_converter,
                                   propagate_selection_to_data=True,
                                   cls=ListItemButton)
        self.adapter=list_adapter



import charac
pSPECIAL=charac.SPECIAL
pcharacterDetails=charac.characterDetails
pperks=charac.perks
pinventory=charac.inventory
pEXP=charac.EXP
player=character(SPECIAL=pSPECIAL,characterDetails=pcharacterDetails,perks=pperks,inventory=pinventory,EXP=pEXP)

presentation=Builder.load_file('main.kv')

class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
    playerCharacter=player
    def reloadCharacter(self):
        import charac
        pSPECIAL=charac.SPECIAL
        pcharacterDetails=charac.characterDetails
        pperks=charac.perks
        pinventory=charac.inventory
        pEXP=charac.EXP
        player=character(SPECIAL=pSPECIAL,characterDetails=pcharacterDetails,perks=pperks,inventory=pinventory,EXP=pEXP)
        return player
    def saveCharacter(self):################### EDIT THIS TO JUST TAKE IT ALL FROM THE SELF.PLAYER OBJECT DIRECTLY
        with open('charac.py','w') as savechar:
            print 'Saving Character'
            preparedString="import weapons as w\nSPECIAL=["
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
            preparedString+='"]\nperks=['
            for perk in self.playerCharacter.perks:
                preparedString+="'"+perk+"',"
            if preparedString[-1]==',':
                preparedString=preparedString[:-1]
            preparedString+=']\ninventory=['
            for item in self.playerCharacter.inventory:
                preparedString+='"'+item+'"'
            if preparedString[-1]==',':
                preparedString=preparedString[:-1]
            preparedString+="]\nEXP={}".format(str(self.playerCharacter.exp))
            savechar.write(preparedString)
        with open(os.path.join('savedchar','char.py'),'w') as savechar:
            print 'Saving Character'
            preparedString="import weapons as w\nSPECIAL=["
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
            preparedString+='"]\nperks=['
            for perk in self.playerCharacter.perks:
                preparedString+="'"+perk+"',"
            if preparedString[-1]==',':
                preparedString=preparedString[:-1]
            preparedString+=']\ninventory=['
            for item in self.playerCharacter.inventory:
                preparedString+='"w.'+item.name.replace(' ','')+'"'
            if preparedString[-1]==',':
                preparedString=preparedString[:-1]
            preparedString+="]\nEXP={}".format(str(self.playerCharacter.exp))
            savechar.write(preparedString)

    def loadCharacter(self,filepath,filename):
        with open(os.path.join(filepath,filename),'r') as loadChar:
            with open('charac.py','w') as currentChar:
                for line in loadChar.readlines():
                    currentChar.write(line)

class SpecialLabel(Label):
    def __init__(self, **kwargs):
        super(SpecialLabel, self).__init__(**kwargs)
    def updateLabel(self,root, XX, i):
        self.text='{}: {}'.format(XX, root.playerCharacter.special[i])

class CharDetailLabel(Label):
    def __init__(self, **kwargs):
        super(CharDetailLabel, self).__init__(**kwargs)
    def updateLabel(self,root,idString,proprty):
        if idString == 'HP':
            self.text = 'HP: {}/{}'.format(root.playerCharacter.HP,root.playerCharacter.maxHP)
        elif idString=='Name':
            self.text='{}: {}'.format(idString,proprty)
        else:
            self.text='{}: {}'.format(str(idString), proprty)

class ArrowButton(Button):
    def __init__(self, **kwargs):
        super(ArrowButton, self).__init__(**kwargs)
        self.background_normal=''
        self.background_color=(0.1,0.1,0.1,1)

class StatLabel(Label):
    def __init__(self, **kwargs):
        super(StatLabel, self).__init__(**kwargs)
        self.background_normal=''
        self.background_color=(0.1,0.1,0.1,1)

class SPECIALrow(BoxLayout):
    def __init__(self, **kwargs):
        super(SPECIALrow, self).__init__(**kwargs)
        self.padding=(5,5)

class characterDetailsInput(TextInput):
    def __init__(self, **kwargs):
        super(characterDetailsInput, self).__init__(**kwargs)
    def getText(self,root,i):
        text=root.playerCharacter.characterDetails[i]
        return str(text)
    def updateText(self,root,i):
        root.playerCharacter.characterDetails[i]=self.text
        root.playerCharacter.updateSPECIALAndcharacterDetails()

class numLabel(Label):
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
        root.playerCharacter.updateSPECIALAndcharacterDetails()

class SkillLabel(Label):
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

'''self,Name,Weight,Value,Description, minST,Dmg,Range,APS,APT,APB'''

class PipBoy(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PipBoy().run()
