#encoding:utf-8
from sys import exit
from random import randint

class Cheat(object):
	"""docstring for Game"""
	def __init__(self):
		pass


	def cheat(self):
		print "You are in a cheat room,you are safe here."
		print "type the room you want to go into"

		next_room=raw_input("type the room name here---->")

		return next_room