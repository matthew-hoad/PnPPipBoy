import weapons as w
import apparels as ap
import aids as ai
import miscs as m
import ammos as am
SPECIAL=[7,3,10,1,5,4,10]
characterDetails=["Dirk Anger","55","Human","Male","-50","Wants nothing more than the sweet embrace of death from a gian gun filled with drugs."]
traits=[['Chem Reliant','''You are more easily addicted to chems.
Your chance to be addicted is twice
normal, but you recover in half the time
from their ill effects. Robots cannot
choose this trait.'''],['Jinxed','''The good thing is that everyone around
you has more critical
failures in combat. The bad
thing is: so do you! If you,
a member of your party, or a
non-player character have a
failure in combat, there is a
greater likelihood the
failure will be upgraded
(downgraded?) to a critical
failure. Critical failures
are bad: weapons explode, you may hit
the wrong target, you could lose part of
your turn, or any number of bad things.
Failures are 50% more likely to become
critical failures around the character
or anyone else in combat.''']]
inventory=[w.weaponM16,w.weaponpoint38SnubnoseSpecial,ap.apparelLeatherDuster,ap.apparelStetson,m.miscDignity,w.weaponBrassKnuckles,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammopoint38Caliber,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm,am.ammo5point56mm]
EXP=0
poisonandrads=[0,0]
smallGuns=45
bigGuns=20
energyWeapons=20
unarmed=60
meleeWeapons=50
throwing=40
firstAid=8
doctor=9
sneak=35
lockpick=23
steal=30
traps=13
science=4
repair=3
pilot=26
speech=50
barter=40
gambling=50
outdoorsman=4
skills=[smallGuns,bigGuns,energyWeapons,unarmed,meleeWeapons,throwing,firstAid,doctor,sneak,lockpick,steal,traps,science,repair,pilot,speech,barter,gambling,outdoorsman]
currentlyEquipped={'weapon':'.38 Snubnose Special','head':'Stetson','body':'Leather Duster','aid':'None','misc':'None','ammo':'.38 Caliber'}
HP=1