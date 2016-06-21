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
    def __init__(self,characterDetails,level,EXP,
        maxHP,HP,rads,poison,wounds,
        karma,SPECIAL,perks,notes,inventory):
        self.name=characterDetails[0]
        self.gender=characterDetails[1]
        self.race=characterDetails[2]
        self.age=characterDetails[3]
        self.Notes=characterDetails[4]


        self.level=level
        self.exp=EXP
        self.karma=karma
        self.ST=SPECIAL.lst[0]
        self.PE=SPECIAL.lst[1]
        self.EN=SPECIAL.lst[2]
        self.CH=SPECIAL.lst[3]
        self.IN=SPECIAL.lst[4]
        self.AG=SPECIAL.lst[5]
        self.LK=SPECIAL.lst[6]

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
        self.throwing=0+4*se;f.AG
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


    def addEXP(exp):
        self.EXP+=exp
        checkLevel()

    def checkLevel():
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

presentation=Builder.load_file('main.kv')

class SPECIALclass:
    def __init__(self,points,lst):
        self.points=points
        self.lst=lst

SPECIAL=SPECIALclass(33,[1,1,1,1,1,1,1])

class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.SPECIAL=import character
    def writeToPlayer(self,**kwargs):
        with open('character.py', 'w') as player:
            if kwargs['SPECIAL']:
                preparedString='SPECIAL = ['
                for litem in kwargs['SPECIAL']:
                    preparedString+=str(litem)+','
                preparedString=preparedString[:-1]
                preparedString+=']\n'
                player.write(preparedString)
            if kwargs['characterDetails']:
                preparedString='characterDetails = ['
                for litem in kwargs['characterDetails']:
                    try:
                        litem=int(litem)
                        preparedString+=str(litem)+','
                    except:
                        preparedString+='"'
                        preparedString+=str(litem)
                        preparedString+='"'+','
                preparedString=preparedString[:-1]
                preparedString+=']\n'
                player.write(preparedString)
    def loadCharacter(self,filepath,filename):
        with open(os.path.join(filepath,filename),'r') as loadChar:
            with open('character.py','w') as currentChar:
                for line in loadChar.readlines():
                    currentChar.write(line)

class ArrowButton(Button):
    def __init__(self, **kwargs):
        super(ArrowButton, self).__init__(**kwargs)
        self.background_normal=''
        self.background_color=(0.1,0.1,0.1,1)
        #self.on_press=self.writetoplayer(SPECIAL=[SPECIAL.lst[0],SPECIAL.lst[1],SPECIAL.lst[2],SPECIAL.lst[3],SPECIAL.lst[4],SPECIAL.lst[5],SPECIAL.lst[6]])

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

    def incrment(self,num):
        if SPECIAL.points!=0 and self.value<10:
            self.value+=num
            SPECIAL.points-=num
        if self.value==10 and num<0:
            self.value+=num
            SPECIAL.points-=num
        if SPECIAL.points==0 and num<0:
            self.value+=num
            SPECIAL.points-=num
        if self.value<1:
            self.value=1
class STnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(STnumLabel, self).__init__(**kwargs)
        self.value=SPECIAL.lst[0]
    def updateNum():
        SPECIAL.lst[0]=self.value
class PEnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(PEnumLabel, self).__init__(**kwargs)
        self.value=SPECIAL.lst[1]
    def updateNum():
        SPECIAL.lst[1]=self.value
class ENnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(ENnumLabel, self).__init__(**kwargs)
        self.value=SPECIAL.lst[2]
    def updateNum():
        SPECIAL.lst[2]=self.value
class CHnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(CHnumLabel, self).__init__(**kwargs)
        self.value=SPECIAL.lst[3]
    def updateNum():
        SPECIAL.lst[3]=self.value
class INnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(INnumLabel, self).__init__(**kwargs)
        self.value=SPECIAL.lst[4]
    def updateNum():
        SPECIAL.lst[4]=self.value
class AGnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(AGnumLabel, self).__init__(**kwargs)
        self.value=SPECIAL.lst[5]
    def updateNum():
        SPECIAL.lst[5]=self.value
class LKnumLabel(numLabel):
    def __init__(self, **kwargs):
        super(LKnumLabel, self).__init__(**kwargs)
        self.value=SPECIAL.lst[6]
    def updateNum():
        SPECIAL.lst[6]=self.value


class PipBoy(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PipBoy().run()
