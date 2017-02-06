from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
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
from functools import partial
from kivy.resources import resource_add_path
from kivy.uix.effectwidget import EffectWidget
from effectwidget import EffectWidget

class PlayerTrait:
    def __init__(self,name,desc):
        self.name=name
        self.desc=desc

class PipLabel(Label):
    def __init__(self, **kwargs):
        super(PipLabel, self).__init__(**kwargs)
        #self.canvas.add(Color(0,0.5,0,0.5))
        #bcolor = ListProperty([0,0,0,0])

class PipLabel2(PipLabel):
    def __init__(self, **kwargs):
        super(PipLabel, self).__init__(**kwargs)
        #self.canvas.add(Color(0,0.5,0,0.5))
        #bcolor = ListProperty([0,0,0,0])
        self.size=self.texture_size

class PipButton(Button):
    def __init__(self, **kwargs):
        super(PipButton, self).__init__(**kwargs)

class RemoveItemButton(PipButton):
    def __init__(self, **kwargs):
        super(RemoveItemButton, self).__init__(**kwargs)

class PipToggleButton(ToggleButton):
    def __init__(self, **kwargs):
        super(PipToggleButton, self).__init__(**kwargs)
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

class PipTextInput(TextInput):
    def __init__(self, **kwargs):
        super(PipTextInput, self).__init__(**kwargs)
        #self.background_normal=''
        #self.background_color=(0,0.1,0,1)

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

        self.currentlyEquipped={'weapon':'None','head':'None','body':'None','aid':'None','misc':'None','ammo':'None'}

        self.update()

    def equipItem(self,item):
        self.currentlyEquipped['{}'.format(item.itemType)]=item.name
        #print self.currentlyEquipped

    def removeItem(self,itemtoberemoved):
        try:
            counter=0
            for item in self.inventory:
                if counter==0 and item.name==itemtoberemoved:
                    counter+=1
                    #print self.inventory
                    self.inventory.remove(item)
                    if item.itemType!='ammo':
                        for key, value in self.currentlyEquipped.iteritems():
                            if value==itemtoberemoved:
                                self.currentlyEquipped[key]='None'
                    #print self.inventory
        except:
            pass

    def removeAmmo(self, ammotoberemoved):
        try:
            # print self.inventory
            for item in self.inventory:
                if item.__class__.__name__=='ammo' and item.name==ammotoberemoved:
                    while item in self.inventory:
                        #print 'removing an item'
                        self.inventory.remove(item)
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
        if self.HP<-5:
            self.HP=-5

        self.currentEncumbrance=0.0
        for item in self.inventory:
            self.currentEncumbrance+=item.weight
        self.currentEncumbrance=int(self.currentEncumbrance)
        
        
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

import charac
player=character(SPECIAL=charac.SPECIAL,characterDetails=charac.characterDetails,Traits=charac.traits,inventory=charac.inventory,EXP=charac.EXP)
try:
    player.poison=charac.poisonandrads[0]
    player.rads=charac.poisonandrads[1]
    player.skills=charac.skills
    player.currentlyEquipped=charac.currentlyEquipped
    player.HP=charac.HP
    #print 'HP updated'
except:
    pass
player.update()

resource_add_path('data/images/defaulttheme-0.png')
presentation=Builder.load_file('main.kv')

class MyEffect(EffectWidget):
    def __init__(self, **kwargs):
        super(MyEffect, self).__init__(**kwargs)

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
    playerCharacter=player
    os=os

    def updateTraitsAndWeapons(self,root):
        for childs in root.ids.PlayerTraits.children:
            for child in childs.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton':
                    #print 'Found one!'
                    child.updateAll(root)

    def setEquipped(self,inv):
        foundAnEquippable=False
        foundAnEquippableHead=False
        foundAnEquippableBody=False
        for row in inv.children:
            for child in row.children:
                if child.__class__.__name__=='PipToggleButton' and (child.group not in ['head','body']):
                    if child.state=='down' and foundAnEquippable==False:
                        #print 'Got it'
                        #self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]=row.boundItem.name
                        self.playerCharacter.equipItem(row.boundItem)
                        foundAnEquippable=True
                    elif child.state=='normal' and foundAnEquippable==False:
                        self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]='None'


                elif child.__class__.__name__=='PipToggleButton' and child.group=='head':
                    if child.state=='down' and foundAnEquippableHead==False:
                        #print 'Got it'
                        #self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]=row.boundItem.name
                        self.playerCharacter.equipItem(row.boundItem)
                        foundAnEquippableHead=True
                    elif child.state=='normal' and foundAnEquippableHead==False:
                        self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]='None'


                elif child.__class__.__name__=='PipToggleButton' and child.group=='body':
                    if child.state=='down' and foundAnEquippableBody==False:
                        #print 'Got it'
                        #self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]=row.boundItem.name
                        self.playerCharacter.equipItem(row.boundItem)
                        foundAnEquippableBody=True
                    elif child.state=='normal' and foundAnEquippableBody==False:
                        self.playerCharacter.currentlyEquipped['{}'.format(row.boundItem.itemType)]='None'
        #print self.playerCharacter.currentlyEquipped

    def addToInventory(self,inv,**kwargs):
        foundAnAddable=False
        for row in inv.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and foundAnAddable==False:
                    if child.state=='down':
                        try:
                            #print "count in kwargs['count'] from addToInventory = ",kwargs['count']
                            for i in range(kwargs['count']):
                                self.playerCharacter.inventory.append(row.boundItem)
                        except:
                            self.playerCharacter.inventory.append(row.boundItem)
                        foundAnAddable=True

    def createItem(self,ref,**kwargs):
        NewItemString=''
        if ref=='weapon':
            try:
                NewItemString+="weapon{}=weapon('{}',{},{},{},'{}',{},{},{},'{}',ammoType='{}',magSize={})".format(kwargs['Name'].replace(' ','').replace('.','point'),kwargs['Name'],kwargs['Value'],kwargs['minST'],kwargs['Weight'],kwargs['Dmg'],kwargs['Range'],kwargs['APS'],kwargs['APT'],kwargs['APB'],kwargs['ammoType'],kwargs['magSize'])
            except:
                NewItemString+="weapon{}=weapon('{}',{},{},{},'{}',{},{},{},'{}')".format(kwargs['Name'].replace(' ','').replace('.','point'),kwargs['Name'],kwargs['Value'],kwargs['minST'],kwargs['Weight'],kwargs['Dmg'],kwargs['Range'],kwargs['APS'],kwargs['APT'],kwargs['APB'])
            with open('weapons.py','r') as weapons:
                linelist=[]
                for line in weapons.readlines():
                    linelist.append(line)
            linelist=linelist[1:-1]
            linelist.append(NewItemString)
            decllist=[]
            for line in linelist:
                decllist.append(line.split('=')[0])
            with open('weapons.py','w') as weapons:
                preparedString='from itemclasses import weapon\n'
                for line in linelist:
                    preparedString+=line
                preparedString+='\nWeapons=['
                for decl in decllist:
                    preparedString+=decl+','
                preparedString=preparedString[:-1]
                preparedString+=']'
                weapons.write(preparedString)
        elif ref=='head' or ref=='body':
            NewItemString+="apparel{}=apparel('{}',{},{},{},'{}','{}','{}','{}','{}','{}')".format(kwargs['Name'].replace(' ','').replace('.','point'),kwargs['Name'],kwargs['Value'],kwargs['Weight'],kwargs['AC'],kwargs['N'],kwargs['L'],kwargs['F'],kwargs['P'],kwargs['E'],ref)
            with open('apparels.py','r') as apparels:
                linelist=[]
                for line in apparels.readlines():
                    linelist.append(line)
            linelist=linelist[1:-1]
            linelist.append(NewItemString)
            decllist=[]
            for line in linelist:
                decllist.append(line.split('=')[0])
            with open('apparels.py','w') as apparels:
                preparedString='from itemclasses import apparel\n'
                for line in linelist:
                    preparedString+=line
                preparedString+='\nApparels=['
                for decl in decllist:
                    preparedString+=decl+','
                preparedString=preparedString[:-1]
                preparedString+=']'
                apparels.write(preparedString)
        elif ref=='aid':
            NewItemString+="aid{}=aid('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(kwargs['Name'].replace(' ','').replace('.','point'),kwargs['Name'],kwargs['Value'],kwargs['Weight'],kwargs['HP'],kwargs['Rad'],kwargs['Poison'],kwargs['ST'],kwargs['PE'],kwargs['EN'],kwargs['CH'],kwargs['IN'],kwargs['AG'],kwargs['LK'],kwargs['radRes'],kwargs['poisonRes'])
            with open('aids.py','r') as aids:
                linelist=[]
                for line in aids.readlines():
                    linelist.append(line)
            linelist=linelist[1:-1]
            linelist.append(NewItemString)
            decllist=[]
            for line in linelist:
                decllist.append(line.split('=')[0])
            with open('aids.py','w') as aids:
                preparedString='from itemclasses import aid\n'
                for line in linelist:
                    preparedString+=line
                preparedString+='\nAids=['
                for decl in decllist:
                    preparedString+=decl+','
                preparedString=preparedString[:-1]
                preparedString+=']'
                aids.write(preparedString)
        elif ref=='misc':
            NewItemString+="misc{}=misc('{}',{},{},'''{}''')".format(kwargs['Name'].replace(' ','').replace('.','point'),kwargs['Name'],kwargs['Weight'],kwargs['Value'],kwargs['Description'])
            with open('miscs.py','r') as miscs:
                linelist=[]
                for line in miscs.readlines():
                    linelist.append(line)
            linelist=linelist[1:-1]
            linelist.append(NewItemString)
            decllist=[]
            for line in linelist:
                decllist.append(line.split('=')[0])
            with open('miscs.py','w') as miscs:
                preparedString='from itemclasses import misc\n'
                for line in linelist:
                    preparedString+=line
                preparedString+='\nMiscs=['
                for decl in decllist:
                    preparedString+=decl+','
                preparedString=preparedString[:-1]
                preparedString+=']'
                miscs.write(preparedString)
        elif ref=='ammo':
            NewItemString+="ammo{}=ammo('{}',{},{},{},{})".format(kwargs['Name'].replace(' ','').replace('.','point'),kwargs['Name'],kwargs['Value'],kwargs['Weight'],kwargs['AC'],kwargs['DR'])
            with open('ammos.py','r') as ammos:
                linelist=[]
                for line in ammos.readlines():
                    linelist.append(line)
            linelist=linelist[1:-1]
            linelist.append(NewItemString)
            decllist=[]
            for line in linelist:
                decllist.append(line.split('=')[0])
            with open('ammos.py','w') as ammos:
                preparedString='from itemclasses import ammo\n'
                for line in linelist:
                    preparedString+=line
                preparedString+='\nAmmos=['
                for decl in decllist:
                    preparedString+=decl+','
                preparedString=preparedString[:-1]
                preparedString+=']'
                ammos.write(preparedString)
        else:
            pass

    def deleteItem(self,inv):
        foundAnAddable=False
        for row in inv.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and foundAnAddable==False:
                    if child.state=='down':
                        print 'Got ',child.text
                        item = row.boundItem
                        foundAnAddable=True
        try:
            if item.itemType=='weapon':
                with open('weapons.py','r') as weapons:
                    linelist=[]
                    for line in weapons.readlines():
                        linelist.append(line)
                linelist=linelist[1:-1]
                decllist=[]
                [decllist.append(line.split('=')[0]) for line in linelist]
                try:
                    removeIndex=decllist.index('weapon{}'.format(item.name.replace(' ','').replace('.','point')))
                    decllist.remove('weapon{}'.format(item.name.replace(' ','').replace('.','point')))
                    linelist.remove(linelist[removeIndex])
                except:
                    pass
                with open('weapons.py','w') as weapons:
                    preparedString='from itemclasses import weapon\n'
                    for line in linelist:
                        preparedString+=line
                    preparedString+='Weapons=['
                    for decl in decllist:
                        preparedString+=decl+','
                    if preparedString[-1]==',':
                        preparedString=preparedString[:-1]
                    preparedString+=']'
                    weapons.write(preparedString)

            elif item.itemType=='head' or item.itemType=='body':
                with open('apparels.py','r') as apparels:
                    linelist=[]
                    for line in apparels.readlines():
                        linelist.append(line)
                linelist=linelist[1:-1]
                decllist=[]
                [decllist.append(line.split('=')[0]) for line in linelist]
                try:
                    removeIndex=decllist.index('apparel{}'.format(item.name.replace(' ','').replace('.','point')))
                    decllist.remove('apparel{}'.format(item.name.replace(' ','').replace('.','point')))
                    linelist.remove(linelist[removeIndex])
                except:
                    pass
                with open('apparels.py','w') as apparels:
                    preparedString='from itemclasses import apparel\n'
                    for line in linelist:
                        preparedString+=line
                    preparedString+='Apparels=['
                    for decl in decllist:
                        preparedString+=decl+','
                    if preparedString[-1]==',':
                        preparedString=preparedString[:-1]
                    preparedString+=']'
                    apparels.write(preparedString)

            elif item.itemType=='aid':
                with open('aids.py','r') as aids:
                    linelist=[]
                    for line in aids.readlines():
                        linelist.append(line)
                linelist=linelist[1:-1]
                decllist=[]
                [decllist.append(line.split('=')[0]) for line in linelist]
                try:
                    removeIndex=decllist.index('aid{}'.format(item.name.replace(' ','').replace('.','point')))
                    decllist.remove('aid{}'.format(item.name.replace(' ','').replace('.','point')))
                    linelist.remove(linelist[removeIndex])
                except:
                    pass
                with open('aids.py','w') as aids:
                    preparedString='from itemclasses import aid\n'
                    for line in linelist:
                        preparedString+=line
                    preparedString+='Aids=['
                    for decl in decllist:
                        preparedString+=decl+','
                    if preparedString[-1]==',':
                        preparedString=preparedString[:-1]
                    preparedString+=']'
                    aids.write(preparedString)

            elif item.itemType=='misc':
                with open('miscs.py','r') as miscs:
                    linelist=[]
                    for line in miscs.readlines():
                        linelist.append(line)
                linelist=linelist[1:-1]
                #print linelist
                decllist=[]
                [decllist.append(line.split('=')[0]) for line in linelist]
                try:
                    removeIndex=decllist.index('misc{}'.format(item.name.replace(' ','').replace('.','point')))
                    decllist.remove('misc{}'.format(item.name.replace(' ','').replace('.','point')))
                    linelist.remove(linelist[removeIndex])
                except:
                    pass
                with open('miscs.py','w') as miscs:
                    preparedString='from itemclasses import misc\n'
                    for line in linelist:
                        preparedString+=line
                    preparedString+='Miscs=['
                    for decl in decllist:
                        preparedString+=decl+','
                    if preparedString[-1]==',':
                        preparedString=preparedString[:-1]
                    preparedString+=']'
                    miscs.write(preparedString)
            elif item.itemType=='ammo':
                with open('ammos.py','r') as ammos:
                    linelist=[]
                    for line in ammos.readlines():
                        linelist.append(line)
                linelist=linelist[1:-1]
                #print linelist
                decllist=[]
                [decllist.append(line.split('=')[0]) for line in linelist]
                try:
                    removeIndex=decllist.index('ammo{}'.format(item.name.replace(' ','').replace('.','point')))
                    decllist.remove('ammo{}'.format(item.name.replace(' ','').replace('.','point')))
                    linelist.remove(linelist[removeIndex])
                except:
                    pass
                with open('ammos.py','w') as ammos:
                    preparedString='from itemclasses import ammo\n'
                    for line in linelist:
                        preparedString+=line
                    preparedString+='Ammos=['
                    for decl in decllist:
                        preparedString+=decl+','
                    if preparedString[-1]==',':
                        preparedString=preparedString[:-1]
                    preparedString+=']'
                    ammos.write(preparedString)
            else:
                pass
        except:
            pass


    def saveCharacter(self):
        with open('charac.py','w') as savechar:
            #print 'Saving Character'
            preparedString="import weapons as w\nimport apparels as ap\nimport aids as ai\nimport miscs as m\nimport ammos as am\nSPECIAL=["
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
                if item.__class__.__name__=='weapon':
                    preparedString+='w.'
                    preparedString+='weapon'+item.name.replace(' ','').replace('.','point')+','
                elif item.__class__.__name__=='apparel':
                    preparedString+='ap.'
                    preparedString+='apparel'+item.name.replace(' ','').replace('.','point')+','
                elif item.__class__.__name__=='aid':
                    preparedString+='ai.'
                    preparedString+='aid'+item.name.replace(' ','').replace('.','point')+','
                elif item.__class__.__name__=='misc':
                    preparedString+='m.'
                    preparedString+='misc'+item.name.replace(' ','').replace('.','point')+','
                elif item.__class__.__name__=='ammo':
                    preparedString+='am.'
                    preparedString+='ammo'+item.name.replace(' ','').replace('.','point')+','
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
            preparedString+='\ncurrentlyEquipped={'+"'weapon':'{}','head':'{}','body':'{}','aid':'{}','misc':'{}','ammo':'{}'".format(self.playerCharacter.currentlyEquipped['weapon'],self.playerCharacter.currentlyEquipped['head'],self.playerCharacter.currentlyEquipped['body'],self.playerCharacter.currentlyEquipped['aid'],self.playerCharacter.currentlyEquipped['misc'],self.playerCharacter.currentlyEquipped['ammo'])+'}'
            preparedString+="\nHP={}".format(self.playerCharacter.HP)
            savechar.write(preparedString)
    def countAmmo(self, ammoName):
        itemNames=[]
        for item in self.playerCharacter.inventory:
            itemNames.append(item.name)
        #print  'count from countAmmo = ',itemNames.count(ammoName)
        return itemNames.count(ammoName)

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
        with open('weapons.py','r') as weapons:
            for line in weapons:
                if line[-1]=='\n':
                    exec(line[:-1])
                else:
                    exec(line)
        for item in Weapons:
            if item.__class__.__name__ == 'weapon' and item.name[:len(text)].lower()==text.lower():
                WeaponRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                WeaponRow.add_widget(PipToggleButton(purpose='weapon',text=item.name,height=100,size_hint_x=0.2,group='pdweapon'))#,on_press=root.playerCharacter.equipItem(item)))
                Values=GridLayout(height=100,cols=8,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='Wgt',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='minST',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='Dmg',height=50,size_hint_x=0.22))
                Values.add_widget(PipLabel(text='Rng',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='APS',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='APT',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='APB',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.value),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.minST),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.dmg),height=50,size_hint_x=0.22))
                Values.add_widget(PipLabel(text=str(item.range),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.APS),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.APT),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.APB),height=50,size_hint_x=0.11))
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
        with open('apparels.py','r') as apparels:
            for line in apparels:
                if line[-1]=='\n':
                    exec(line[:-1])
                else:
                    exec(line)
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in Apparels:
            if item.__class__.__name__ == 'apparel' and item.name[:len(text)].lower() == text.lower():
                if item.ApparelType=='head':
                    #self.add_widget(PipLabel(text='Head',halign='left',size_hint_x=1,height=50,width=root.width))
                    ApparelRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='pdhead'))
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
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='pdbody'))#,on_press=root.playerCharacter.equipItem(item)))
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
        with open('aids.py','r') as aids:
            for line in aids:
                if line[-1]=='\n':
                    exec(line[:-1])
                else:
                    exec(line)
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in Aids:
            if item.__class__.__name__ == 'aid' and item.name[:len(text)].lower() == text.lower():
                #print item
                AidRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AidRow.add_widget(PipToggleButton(purpose='aid',text=item.name,height=100,size_hint_x=0.2,group='pdaid'))
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
        with open('miscs.py','r') as miscs:
            for line in miscs:
                if line[-1]=='\n':
                    exec(line[:-1])
                else:
                    exec(line)
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in Miscs:
            #print item
            if item.__class__.__name__ == 'misc' and item.name[:len(text)].lower() == text.lower():
                #print item
                MiscRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                MiscRow.add_widget(PipToggleButton(purpose='misc',text=item.name,height=100,size_hint_x=0.2,group='pdmisc'))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=2,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                MiscRow.add_widget(Values)
                self.add_widget(MiscRow)
        self.bind(minimum_height=self.setter('height'))

class PreDefinedAmmoInventory(GridLayout):
    def __init__(self, **kwargs):
        super(PreDefinedAmmoInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def search(self,text,root):
        with open('ammos.py','r') as ammos:
            for line in ammos:
                if line[-1]=='\n':
                    exec(line[:-1])
                else:
                    exec(line)
        self.add_widget(PipLabel(text='',height=100,width=root.width))
        for item in Ammos:
            #print item
            if item.__class__.__name__ == 'ammo' and item.name[:len(text)].lower() == text.lower():
                #print item
                AmmoRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AmmoRow.add_widget(PipToggleButton(purpose='misc',text=item.name,height=100,size_hint_x=0.2,group='pdammo'))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=3,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Count',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                Values.add_widget(TextInput(text='0',height=50,width=root.width*0.083))
                AmmoRow.add_widget(Values)
                self.add_widget(AmmoRow)
        paddingrows=GridLayout(rows=4,cols=1,row_default_height=100,row_force_default=True)
        paddingrows.add_widget(Label(text=''))
        paddingrows.add_widget(Label(text=''))
        paddingrows.add_widget(Label(text=''))
        paddingrows.add_widget(Label(text=''))
        self.add_widget(paddingrows)
        self.bind(minimum_height=self.setter('height'))

    def getCount(self):
        try:
            foundACountable=False
            for row in self.children:
                for child in row.children:
                    #print child.__class__.__name__
                    if child.__class__.__name__=='PipToggleButton':
                        if child.state=='down' and foundACountable==False:
                            #print 'Got it'
                            count=int(row.children[-2].children[0].text)
                            foundACountable=True
                        elif child.state=='normal' and foundACountable==False:
                            pass

            #print 'count from getCount = ',count
            return count
        except:
            return 0

class WeaponInventory(GridLayout):
    def __init__(self, **kwargs):
        super(WeaponInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(Label(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'weapon':
                WeaponRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                WeaponRow.add_widget(PipToggleButton(purpose='weapon',text=item.name,height=100,size_hint_x=0.2,group='weapon'))
                Values=GridLayout(height=100,cols=8,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='Wgt',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='minST',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='Dmg',height=50,size_hint_x=0.22))
                Values.add_widget(PipLabel(text='Rng',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='APS',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='APT',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text='APB',height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.value),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.minST),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.dmg),height=50,size_hint_x=0.22))
                Values.add_widget(PipLabel(text=str(item.range),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.APS),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.APT),height=50,size_hint_x=0.11))
                Values.add_widget(PipLabel(text=str(item.APB),height=50,size_hint_x=0.11))
                WeaponRow.add_widget(Values)
                self.add_widget(WeaponRow)
        self.bind(minimum_height=self.setter('height'))

    def pressEquipped(self,root):
        foundEquipped=False
        for row in self.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and child.text==root.playerCharacter.currentlyEquipped['weapon'] and foundEquipped==False:
                    foundEquipped=True
                    child.state='down'

class ApparelInventory(GridLayout):
    def __init__(self, **kwargs):
        super(ApparelInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(Label(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'apparel':
                if item.ApparelType=='head':
                    #self.add_widget(PipLabel(text='Head',halign='left',size_hint_x=1,height=50,width=root.width))
                    ApparelRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='head'))
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
                    ApparelRow.add_widget(PipToggleButton(purpose='apparel',text=item.name,height=100,size_hint_x=0.2,group='body'))
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
    def pressEquipped(self,root):
        foundEquippedHead=False
        foundEquippedBody=False
        #print root.playerCharacter.currentlyEquipped
        for row in self.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and child.text==root.playerCharacter.currentlyEquipped['head'] and foundEquippedHead==False:
                    foundEquippedHead=True
                    child.state='down'
        for row in self.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and child.text==root.playerCharacter.currentlyEquipped['body'] and foundEquippedBody==False:
                    foundEquippedBody=True
                    child.state='down'

class AidInventory(GridLayout):
    def __init__(self, **kwargs):
        super(AidInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(Label(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'aid':
                #print item
                AidRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AidRow.add_widget(PipToggleButton(purpose='aid',text=item.name,height=100,size_hint_x=0.2,group='aid'))
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
    
    def pressEquipped(self,root):
        foundEquipped=False
        for row in self.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and child.text==root.playerCharacter.currentlyEquipped['aid'] and foundEquipped==False:
                    foundEquipped=True
                    child.state='down'

class MiscInventory(GridLayout):
    def __init__(self, **kwargs):
        super(MiscInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(Label(text='',height=100,width=root.width))
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'misc':
                #print item
                MiscRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                MiscRow.add_widget(PipToggleButton(purpose='misc',text=item.name,height=100,size_hint_x=0.2,group='misc'))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=2,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                MiscRow.add_widget(Values)
                self.add_widget(MiscRow)
        self.bind(minimum_height=self.setter('height'))

    def pressEquipped(self,root):
        foundEquipped=False
        for row in self.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and child.text==root.playerCharacter.currentlyEquipped['misc'] and foundEquipped==False:
                    foundEquipped=True
                    child.state='down'

class AmmoInventory(GridLayout):
    def __init__(self, **kwargs):
        super(AmmoInventory, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.cols=1
        self.spacing=10
        self.size_hint_y=None

    def populate(self,root):
        self.add_widget(Label(text='',height=100,width=root.width))
        alreadyThere=[]
        for item in root.playerCharacter.inventory:
            if item.__class__.__name__ == 'ammo' and item.name not in alreadyThere:
                #print item
                #print root.playerCharacter.inventory
                alreadyThere.append(item.name)
                AmmoRow=ItemRow(height=100,size_hint_x=1,size_hint_y=None,miminum_height=100,spacing=5,boundItem=item)
                AmmoRow.add_widget(PipToggleButton(purpose='misc',text=item.name,height=100,size_hint_x=0.2,group='ammo'))
                Values=GridLayout(height=100,size_hint_x=0.7,cols=3,rows=2)
                Values.add_widget(PipLabel(text='Val',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Wgt',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text='Count',height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.value),height=50,width=root.width*0.083))
                Values.add_widget(PipLabel(text=str(item.weight),height=50,width=root.width*0.083))
                CountBox=BoxLayout(spacing=5)
                RemoveBullet=PipButton(text='[-]')
                def remI(self):
                    return root.playerCharacter.removeItem(self.parent.parent.parent.boundItem.name)
                def addI(self):
                    return root.playerCharacter.inventory.append(self.parent.parent.parent.boundItem)
                def upd8PL(self):
                    #print self.parent
                    #print self.parent.children
                    for child in self.parent.children:
                        if child.__class__.__name__=='PipLabel':
                            child.text=str(root.countAmmo(self.parent.parent.parent.boundItem.name))
                    # self..clear_widgets(children=None)
                    # self..populate(root)
                RemoveBullet.bind(on_press=remI,on_release=upd8PL)
                #removepartial=partial(root.playerCharacter.removeItem)
                #RemoveBullet.bind(on_release=removepartial(item))
                CountBox.add_widget(RemoveBullet)
                CountBox.add_widget(PipLabel(text=str(root.countAmmo(item.name))))
                AddBullet=PipButton(text='[+]')
                AddBullet.bind(on_press=addI,on_release=upd8PL)
                CountBox.add_widget(AddBullet)
                Values.add_widget(CountBox)
                AmmoRow.add_widget(Values)
                self.add_widget(AmmoRow)
        self.bind(minimum_height=self.setter('height'))

    def pressEquipped(self,root):
        foundEquipped=False
        for row in self.children:
            for child in row.children:
                #print child.__class__.__name__
                if child.__class__.__name__=='PipToggleButton' and child.text==root.playerCharacter.currentlyEquipped['ammo'] and foundEquipped==False:
                    foundEquipped=True
                    child.state='down'

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
