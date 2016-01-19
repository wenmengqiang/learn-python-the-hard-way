#encoding:utf-8
from sys import exit
from random import randint

class Death(object):
	"""docstring for Game"""
	def __init__(self):	
		self.equips=[
			"You died.You kinda suck at this.",
			"Your mom wou ld be proud.If she were smarter.",
			"Such a luser!!"
		]
		pass


	def death(self):
		print self.equips[randint(0,len(self.equips)-1)]
		return 'game_over'