#encoding:utf-8
from sys import exit
from random import randint

class TheBridge(object):
	"""docstring for Game"""
	def __init__(self):
		pass
		
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
