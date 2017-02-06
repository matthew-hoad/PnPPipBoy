class PlayerTrait:
	def __init__(self,name,desc):
		self.name=name
		self.desc=desc

FastMetabolism=PlayerTrait('Fast Metabolism','''Your metabolic rate is twice normal.
This means that you are much less
resistant to radiation and poison, but
your body heals faster. You get a 2
point bonus to Healing Rate, but your
Radiation and Poison Resistance start at
0% (racial modifiers are added later).
Robots cannot choose this trait.''')
Bruiser=PlayerTrait('Bruiser','''A little slower, but a little bigger.
You may not hit as often, but they will
feel it when you do! Your total action
points are lowered, but your Strength is
increased. You get a 2 point bonus to
Strength, but loose 2 Action Points.
Small Frame
You are not quite as big as everyone
else, but that never slowed you down.
You can't carry as much, but you are
more agile. You get a 1 point bonus to
Agility, but your Carry Weight is only
15 lbs X Strength.''')
OneHander=PlayerTrait('One Hander','''One of your hands is very dominant. You
excel with single-handed weapons, but
two-handed weapons cause a problem. You
have a 40% penalty to hit with twohanded
weapons, but get a 20% bonus to
hit with weapons that only require one
hand. Animals cannot choose this trait.''')
Finesse=PlayerTrait('Finesse','''Your attacks show a lot of finesse. You
don't do as much damage, but you cause
more critical hits. All of your attacks
lose 30% of their damage (after
reductions are made for Damage
Resistance, etc.) but you gain a 10%
bonus to Critical Chance.''')
Kamikaze=PlayerTrait('Kamikaze','''By not paying attention to any threats,
you can act a lot faster in a turn.
This lowers your Armor Class to just
what you are wearing, but you sequence
much faster in a combat turn. You have
no natural Armor Class (Armor Class is 
12
therefore 0 regardless of Agility). You
must wear armor to get an Armor Class.
Your sequence gets a 5 point bonus.''')
HeavyHanded=PlayerTrait('Heavy Handed','''You swing harder, not better. Your
attacks are very brutal, but lack
finesse. You rarely cause a good
critical hit, but you always do more
melee damage. You get a 4 point bonus
to Melee Damage, but your critical hits
do 30% less damage, and are 30% less
likely to cripple a limb or cause
unconsciousness.''')
FastShot=PlayerTrait('Fast Shot','''You don't have time for a targeted
attack, because you attack faster than
normal people. It costs you one less
action point to use a weapon. You
cannot perform targeted shots, but all
weapons take one less action point to
use. Note that the Fast Shot trait has
no effect on HtH or Melee attacks.
Animals cannot choose this trait.''')
BloodyMess=PlayerTrait('Bloody Mess','''By some strange twist of fate, people
around you die violently. You always
see the worst way a person can die.
This does not mean you kill them any
faster or slower, but when they do die,
it will be dramatic. Just how dramatic
is up to the Gamemaster.''')
Jinxed=PlayerTrait('Jinxed','''The good thing is that everyone around
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
or anyone else in combat.''')
GoodNatured=PlayerTrait('Good Natured','''You studied less-combative skills as you
were growing up. Your combat skills
start at a lower level, but First Aid,
Doctor, Speech, and Barter are
substantially improved. Those skills
get a 20% bonus. You get a 10% penalty
to starting combat skills (Small Guns,
Big Guns, Energy Weapons, Unarmed, and
Melee Weapons). This is a one-time
bonus. Animals and robots cannot choose
this trait.''')
ChemReliant=PlayerTrait('Chem Reliant','''You are more easily addicted to chems.
Your chance to be addicted is twice
normal, but you recover in half the time
from their ill effects. Robots cannot
choose this trait.''')
ChemResistant=('Chem Resistant','''Chems only effect you half as long as
normal, but your chance to be addicted
is only 50% the normal amount. Robots
cannot choose this trait.''')
NightPerson=PlayerTrait('Night Person','''As a night-time person, you are more
awake when the sun goes down. Your
Intelligence and Perception are improved
at night but are dulled during the day.
You get a 1 point penalty to these
Statistics from 0601 to 1800, and a 1
point bonus to these Stats from 1801 to
0600. Robots cannot choose this trait.
Note that the bonus cannot take IN and
PE above the character's racial maximum
or below the character's racial minimum.''')
Skilled=PlayerTrait('Skilled','''Since you spend more time improving your
skills than a normal person, you gain
more skill points. The tradeoff is that
you do not gain as many extra abilities.
You will gain a perk at one level higher
than normal. For example, if you
normally gained a perk every 4 levels,
you would now gain a perk every 5
levels. You will get an additional 5
skill points per new experience level,
and a one-time bonus of +10% to your
skills when you begin the game. Animals
and robots cannot choose this trait.''')
Gifted=PlayerTrait('Gifted','''You have more innate abilities than
most, so you have not spent as much time
honing your skills. Your statistics are
better than the average person, but your
skills are lacking. All Stats get a 1-
point bonus, but all skills get a 10%
penalty and you receive 5 less Skill
Points per level. Robots cannot choose
this trait.''')
SexAppeal=PlayerTrait('Sex Appeal','''This trait increases your chances of
having a good reaction with members of
the opposite sex. Unfortunately, this
trait tends to annoy members of your 
sex. Jealous twits. When interacting
with members of the opposite sex, you
gain a 1 point bonus to Charisma for
reactions only. When making Speech and
Barter rolls, you gain a 40% bonus for
each. When interacting with members of
the same sex, you have a 1 point penalty
to Charisma for reactions only and have
a 40% penalty to both Speech and Barter
rolls. Only humans can choose this
trait.''')
GlowingOne=PlayerTrait('Glowing One','''Extreme radiation exposure has left you
glowing in the dark. Your glow
eliminates modifiers from light in
combat for both you and your enemies.
In addition, you gain a +50% bonus to
Radiation Resistance, but everyone
around you takes 10 rads per hour. 
Only Ghouls can choose this
trait.''')
TechWizard=PlayerTrait('Tech Wizard','''You spent your formative years hunched
over a bench learning all about the way
things work. The trouble is that you've
ruined your eyes! You get a +15% bonus
to Science, Repair, and Lockpick skills,
but you lose 1 Perception. Deathclaws
and Dogs cannot choose this trait.
Fear the Reaper
You have cheated death! You gain perks
as if you were a human, but you are now
on death's short list. This means that
once a month, you must roll against Luck
or else drop dead. Only Ghouls can
choose this trait.''')
VatSkin=PlayerTrait('Vat Skin','''Other people find you hideous to behold
and disgusting to smell after your "dip"
in the FEV vats. The good news is that
you gain a +10 bonus to your Armor Class
thanks to your extra-tough skin. The
bad news is that everyone within ten
hexes of your location, friend and foe,
suffers a 1-point penalty to Perception
(you are unaffected). Only Mutants can
choose this trait.''')
HamFisted=PlayerTrait('Ham Fisted','''Genetic engineering - or dumb luck - has
endowed you with huge hands. You get a
"free" tag skill in Unarmed, but you
suffer a -20% penalty to Small Guns,
First Aid, Doctor, Repair, Science, and
Lockpick Skills (these numbers cannot go
below 0%). Only Mutants can choose this
trait. ''')


AvailableTraits=[FastMetabolism, Bruiser, OneHander, Finesse, Kamikaze, HeavyHanded, FastShot, BloodyMess, Jinxed, GoodNatured, ChemReliant, NightPerson, Skilled, Gifted, SexAppeal, GlowingOne, TechWizard, VatSkin, HamFisted]