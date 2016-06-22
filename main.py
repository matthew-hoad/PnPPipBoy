from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from math import floor
import os

class character:
    def __init__(self,SPECIAL,characterDetails,perks,inventory,EXP):
        self.name=characterDetails[0]
        self.gender=characterDetails[1]
        self.race=characterDetails[2]
        self.age=characterDetails[3]
        self.karma=characterDetails[4]
        self.notes=characterDetails[5]

        if self.race == 'Human':
            self.SPECIALpoints=40
        elif self.race == 'Super Mutant':
            self.SPECIALpoints=40
        elif self.race == 'Ghoul':
            self.SPECIALpoints=42

        self.exp=EXP
        self.level=0

        self.special=SPECIAL
        self.ST=SPECIAL[0]
        self.PE=SPECIAL[1]
        self.EN=SPECIAL[2]
        self.CH=SPECIAL[3]
        self.IN=SPECIAL[4]
        self.AG=SPECIAL[5]
        self.LK=SPECIAL[6]

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

import charac
pSPECIAL=charac.SPECIAL
pcharacterDetails=charac.characterDetails
pperks=charac.perks
pinventory=charac.inventory
pEXP=charac.EXP
player=character(SPECIAL=pSPECIAL,characterDetails=pcharacterDetails,perks=pperks,inventory=pinventory,EXP=pEXP)

presentation=Builder.load_file('main.kv')

#class SPECIALclass:
#    def __init__(self,points,lst):
#        self.points=points
#        self.lst=lst

#SPECIAL=SPECIALclass(33,[1,1,1,1,1,1,1])

class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
    playerCharacter=player
    def writeToPlayer(self,**kwargs):################### EDIT THIS TO JUST TAKE IT ALL FROM THE SELF.PLAYER OBJECT DIRECTLY
        # with open('character.py', 'w') as player:
        #     if kwargs['SPECIAL']:
        #         preparedString='SPECIAL = ['
        #         for litem in kwargs['SPECIAL']:
        #             preparedString+=str(litem)+','
        #         preparedString=preparedString[:-1]
        #         preparedString+=']\n'
        #         player.write(preparedString)
        #     if kwargs['characterDetails']:
        #         preparedString='characterDetails = ['
        #         for litem in kwargs['characterDetails']:
        #             try:
        #                 litem=int(litem)
        #                 preparedString+=str(litem)+','
        #             except:
        #                 preparedString+='"'
        #                 preparedString+=str(litem)
        #                 preparedString+='"'+','
        #         preparedString=preparedString[:-1]
        #         preparedString+=']\n'
        #         player.write(preparedString)
        #     if kwargs['perks']:
        #         pass#####################################   FILL THIS IN
        #     if kwargs['inventory']:
        #         pass#####################################
        #     if kwargs['EXP']:
        #         pass#####################################
        pass
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

class STnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(STnumLabel, self).__init__(**kwargs)
    def getNum(self,root):
        self.value=root.playerCharacter.special[0]
        return self.value
    def updateNum(self,root):
        root.playerCharacter.special[0]=self.value
class PEnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(PEnumLabel, self).__init__(**kwargs)
    def getNum(self,root):
        self.value=root.playerCharacter.special[1]
        return self.value
    def updateNum(self,root):
        root.playerCharacter.special[1]=self.value
class ENnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(ENnumLabel, self).__init__(**kwargs)
    def getNum(self,root):
        self.value=root.playerCharacter.special[2]
        return self.value
    def updateNum(self,root):
        root.playerCharacter.special[2]=self.value
class CHnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(CHnumLabel, self).__init__(**kwargs)
    def getNum(self,root):
        self.value=root.playerCharacter.special[3]
        return self.value
    def updateNum(self,root):
        root.playerCharacter.special[3]=self.value
class INnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(INnumLabel, self).__init__(**kwargs)
    def getNum(self,root):
        self.value=root.playerCharacter.special[4]
        return self.value
    def updateNum(self,root):
        root.playerCharacter.special[4]=self.value
class AGnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(AGnumLabel, self).__init__(**kwargs)
    def getNum(self,root):
        self.value=root.playerCharacter.special[5]
        return self.value
    def updateNum(self,root):
        root.playerCharacter.special[5]=self.value
class LKnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(LKnumLabel, self).__init__(**kwargs)
    def getNum(self,root):
        self.value=root.playerCharacter.special[6]
        return self.value
    def updateNum(self,root):
        root.playerCharacter.special[6]=self.value


class PipBoy(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PipBoy().run()
