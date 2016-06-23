from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
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

        self.exp=EXP
        self.level=0

        self.special=SPECIAL
        self.ST=self.special[0]
        self.PE=self.special[1]
        self.EN=self.special[2]
        self.CH=self.special[3]
        self.IN=self.special[4]
        self.AG=self.special[5]
        self.LK=self.special[6]

        self.maxHP=15 + (self.ST + (2*self.EN))

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
        self.unarmed=30+2*(self.AG*self.ST)
        self.meleeWeapons=20+2*(self.AG*self.ST)
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
    def updateSPECIALAndcharacterDetails():
        self.ST=self.special[0]
        self.PE=self.special[1]
        self.EN=self.special[2]
        self.CH=self.special[3]
        self.IN=self.special[4]
        self.AG=self.special[5]
        self.LK=self.special[6]
        self.name=self.characterDetails[0]
        self.gender=self.characterDetails[1]
        self.race=self.characterDetails[2]
        self.age=self.characterDetails[3]
        self.karma=self.characterDetails[4]
        self.notes=self.characterDetails[5]

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
    def saveCharacter(self):################### EDIT THIS TO JUST TAKE IT ALL FROM THE SELF.PLAYER OBJECT DIRECTLY
        with open('charac.py','w') as savechar:
            print 'Saving Chatacter'
            preparedString="SPECIAL=["
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
            preparedString+="]\ncharacterDetails=['"
            preparedString+=str(self.playerCharacter.name)
            preparedString+="','"
            preparedString+=str(self.playerCharacter.gender)
            preparedString+="','"
            preparedString+=str(self.playerCharacter.race)
            preparedString+="','"
            preparedString+=str(self.playerCharacter.age)
            preparedString+="','"
            preparedString+=str(self.playerCharacter.karma)
            preparedString+="','"
            preparedString+=str(self.playerCharacter.notes)
            preparedString+="']\nperks=["
            for perk in self.playerCharacter.perks:
                preparedString+="'"+perk+"',"
            preparedString=preparedString[:-1]
            preparedString+=']\ninventory=['
            for item in self.playerCharacter.inventory:
                preparedString+="'"+item+"',"
            preparedString=preparedString[:-1]
            preparedString+="]\nEXP={}".format(str(self.playerCharacter.exp))
            savechar.write(preparedString)

    def loadCharacter(self,filepath,filename):
        with open(os.path.join(filepath,filename),'r') as loadChar:
            with open('charac.py','w') as currentChar:
                for line in loadChar.readlines():
                    currentChar.write(line)

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

class numLabel(Label):
    def __init__(self, **kwargs):
        super(numLabel, self).__init__(**kwargs)
    value = NumericProperty(1)

    def incrment(self,root,num):
        if root.playerCharacter.SPECIALpoints!=0 and self.value<10:
            self.value+=num
            root.playerCharacter.SPECIALpoints-=num
        if self.value==10 and num<0:
            self.value+=num
            root.playerCharacter.SPECIALpoints-=num
        if root.playerCharacter.SPECIALpoints==0 and num<0:
            self.value+=num
            root.playerCharacter.SPECIALpoints-=num
        if self.value<1:
            self.value=1
    def getNum(self,root,i):
        text=root.playerCharacter.special[i]
        return str(text)
    def updateNum(self,root,i):
        root.playerCharacter.special[i]=self.text


class PipBoy(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PipBoy().run()
