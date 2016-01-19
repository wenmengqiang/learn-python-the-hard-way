#encoding:utf-8
from sys import exit
from random import randint
from ex42_Map import Map

class Engine(object):
		"""docstring for Engine"""
		def __init__(self):
			super(Engine, self).__init__()
			# self.start = start

		def play(self,map):
			route=['death','central_corridor','laser_weapon_armony','the_bridge','escape_pod','cheat']
			# for map.cur_map in route:
			# 	map.cur_map()
			while map.cur_map in route:
				if map.cur_map=='death':
					map.cur_map=map.death()
					# map.cur_map=map.death()

				elif map.cur_map=='central_corridor':
					map.cur_map=map.central_corridor()
					# map.cur_map=map.central_corridor()

				elif map.cur_map=='laser_weapon_armony':
					map.cur_map=map.laser_weapon_armony()

				elif map.cur_map=='the_bridge':
					map.cur_map=map.the_bridge()

				elif map.cur_map=='escape_pod':
					map.cur_map=map.escape_pod()

				elif map.cur_map=='cheat':
					map.cur_map=map.cheat()

			print "GAME OVER!"
			exit(0)
			# print "\n--------%s"%Map.cur_map
			# next=map.cur_map
#初始化进入的房间
# 			while True:
# 				print "\n--------"
# 				# room=getattr(self,next)
# #获取当前房间的房间号，也就是函数名	
# 				# Map.next()
# 				next=map.cur_map
# 				map.next()
				# Map.cur_map=next()
				# map.cur_map=map.cur_map()
				# return next
#获取下一个房间的房间号，也就是函数名

A_map=Map("central_corridor")
# map='central_corridor'
# A_game=Engine(A_map)
A_game=Engine()
A_game.play(A_map)
#作为引擎，必须知道有哪些地图，现在命名route变量，存入地图名称
#ex42.py注释案例，打鬼子给我了极大的帮助