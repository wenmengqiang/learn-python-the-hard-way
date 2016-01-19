# #encoding:utf-8
# class TheThing(object):
# 	"""docstring for TheThing"""
# 	def __init__(self):
# 		self.number=0

# 	def some_function(self):
# 		print "I got called."

# 	def add_me_up(self,more):
# 		self.number+=more
# 		return self.number
	
# #two different things
# a=TheThing()
# b=TheThing()
# a.some_function()
# b.some_function()

# print a.add_me_up(20)
# print a.add_me_up(30)
# print b.add_me_up(20)
# print b.add_me_up(30)

# print a.number
# print b.number

from sys import exit
from random import randint

class Game(object):
	"""docstring for Game"""
	def __init__(self, start):
		self.start = start
		self.equips=[
			"You died.You kinda suck at this.",
			"Your mom would be proud.If she were smarter.",
			"Such a luser!!"
		]

	def play(self):
		next=self.start
#初始化进入的房间
		while True:
			print "\n--------"
			room=getattr(self,next)
#获取当前房间的房间号，也就是函数名	
			next=room()
#获取下一个房间的房间号，也就是函数名

	def death(self):
		print self.equips[randint(0,len(self.equips)-1)]
		exit(1)

	def central_corridor(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew.You are the last suiviving member and your last"
		print "mission is to get the neutron destruct bomb from the weapons Armory"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "excape pod."
		print "\n"
		print "You're running down the central_corridor to the weapons Armory when"
		print "a Gothon jumps out,red scaly skin,dark grimy teeth,and evil clown costume"
		print "flowing around his hate filled body.He's blocking the door to the "
		print "Armory and about to pull a weapon to blast you."

		action=raw_input("->")

		if action== "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body,which throws"
			print "off your aim.Your laser hits his costume but misses him entirely.This"
			print "completely ruins his burand new costume his mother bought him,which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead.Then he eats you ."
			return 'death'

		elif action=="dodge!":
			print "Like a world class boxer you dodge,weave,slip and slide right"
			print "as the Gothon's blaster cranke a laser past your head."
			print "In the middle of your artful dodge your foot slips and you "
			print "bang you head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return "death"

		elif action=="tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb ang,jura fur fvgf nebhaq gur ubhfr,fur fvgf nebhaq gur ubhfr"
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down,then jump through the weapon Armory door."
			return 'laser_weapon_armony'

		elif action=="cheat":
			return 'cheat'

		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

	def laser_weapon_armony(self):
		print "You do a dive roll into the weapon Armory,crouch and scan the room"
		print "for more Gothons that might be hiding.It's dead quiet ,too quiet."
		print "You stand up and run to the far side of the room and find the "
		print "neutron bomb in its container.There's a keypad lock on the box"
		print "and you need the code to get the bomb out.If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb.The code is 3 digits."
		code="%d%d%d"%(randint(1,9),randint(1,9),randint(1,9))
		guess=raw_input("[keypad]>")
		guesses=0

		while guess!=code and guesses<10:
			print "BZZZZZZEDDDD!"
			guesses+=1
			guess=raw_input("[keypad]>")

		if guess==code:
			print "The container clicks open and the seal breaks,letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'

		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there,and finally the Gothons blow up the "
			print "ship from their ship and you die."
			return 'death'


	def the_bridge(self):
		print "You burst onto the bridge with the neutron destruct bomb"
		print "under your arm and suiprise 5 Gothons who are trying to"
		print "take control of the ship.Each of them has an ever uglier"
		print "clown costume than the last.They haven't pulled their"
		print "weapons out yet,as they see the active bomb under your "
		print "arm and don't want to set it off."

		action=raw_input("->")

		if action=="throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.Right as you drop it a "
			print "Gothon shoots you right in your back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb.You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'

		elif action=="slowly place the bomb":
			print "You point your blaser at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door,open it ,and then carefully"
			print "place the bomb on the floor,pointing your blaster at it."
			print "You then jump back through the door,punch the close button"
			print "and blast the lock so the Gothon can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'

		elif action=="cheat":
			return 'cheat'
	
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"

	def escape_pod(self):
		print "You rush through the ship desperately trying to make it to "
		print "the escape pod before the whole ship explodes.It seem Like"
		print "hardly any Gothon are on the ship,so your run is clear of"
		print "inerference.You get to the chamber with the escape pods,and"
		print "now need to pick one to take.Some of them could be damaged"
		print "but you don't have time to look.There's 5pods,which one"
		print "do you take?"

		good_pod=randint(1,5)
		guess=raw_input("[pod #]>")

		if int(guess)!=good_pod:
			print "You jump into pod %s and hit the eject button."%guess
			print "The pod escapes out into the void of space,then"
			print "implodes as the hull ruptures,crushing your body"
			print "into jam jelly."
			return 'death'

		else:
			print "You jump into pod %s and hit the eject button."%guess
			print "The pod easily slides out into space heading to"
			print "the planet below.As it flies to the planet,you look"
			print "back and see your ship implode then explode like a"
			print "bright star,taking out the Gothon ship at the same"
			print "time.You won!"
			exit(0)

	def cheat():
		print "You are in a cheat room,you are safe here."
		print "type the room you want to go into"

		next_room=raw_input("type the room name here---->")

		return next_room
	

	
a_game=Game("central_corridor")
a_game.play()

#__dict__ python的每个module和每个class都会默认把你这个module和class里的所有object        (你应该知道python里一切皆为object)
#建立一个由name到object的映射(reference)，完全和一个普通的dict/{}一样
#当你print *.__dict__时，就会输出这个dict
#当你print *.__dict__.keys()，module和class里的所有object的名字
##########参考代码"""Jerry Cool's demo for friend."""
#!/usr/bin/env python
# -*- coding: cp936 -*-
################################# 
# class Me(object):
#     """这就是我啦。
#     """
#     def __init__(self,weapon = gun):  # gun 可能是基本类型，也可能是一个类
#         self.__weapon = weapon        # 私有成员变量
#     def fireAt(self,enemy):
#         """向敌人发起攻击，敌人根据被攻击武器种类失血。
#         这里通过调用对方类的方法实现。我看得教材里说'看起来直接通过对方类来
#         调用它的方法很不礼貌，但是这要比直接调用对方类的成员变量要绅士的多'
#         """
#         enemy.beShooted(WeaponKind = self.__weapon)
         
# class Enemy(object):
#     """这就是鬼子
#     """
#     def __init__(self,kind):
#         self.__kind = kind    # 通过设置property调用的私有成员变量
#         self.__health = 100   # 通过自己的方法调用的私有成员变量
#     def beShooted(self,WeaponKind):
#         """失血，通过其它类调用"""
#         if WeaponKind == gun:
#             self.__health -= 10
     
#     @property                  # 2.6 新增
#     def kind(self):
#         """设置成员变量为property,让它可以通过如enemy1.kind调用。不设为公用的原因
#         是可以控制它的access ability,如@kind.setter，@kind.deleter，而且可以附
#         加其它需要的操作
#         """
#         return self.__kind
 
# # 应用实例
# me = Me()
# guiZi = Enemy("boss")
 
# print(guiZi.kind)
# me.fireAt(guiZi)