#encoding:utf-8
from sys import exit
from random import randint
from ex43_Death import Death
from ex43_Central_corridor import CentralCorridor
from ex43_Laser_weapon_armony import LaserWeaponArmony
from ex43_The_bridge import TheBridge
from ex43_Escape_pod import EscapePod
from ex43_Cheat import Cheat

class Engine(object):
		"""docstring for Engine"""
		def __init__(self,xiansuo):
			super(Engine, self).__init__()
			self.xiansuo=xiansuo
			#引擎初始化的时候，给出第一个地图

		def play(self,map0,map1,map2,map3,map4,map5):
			#play函数的参数为6个类，直接调用每个类里的对应函数
			route=['death','central_corridor','laser_weapon_armony','the_bridge','escape_pod','cheat']
			while self.xiansuo in route:
				if self.xiansuo=='death':
					self.xiansuo=map0.death()

				elif self.xiansuo=='central_corridor':
					self.xiansuo=map1.central_corridor()
					
				elif self.xiansuo=='laser_weapon_armony':
					self.xiansuo=map2.laser_weapon_armony()

				elif self.xiansuo=='the_bridge':
					self.xiansuo=map3.the_bridge()

				elif self.xiansuo=='escape_pod':
					self.xiansuo=map4.escape_pod()

				elif self.xiansuo=='cheat':
					self.xiansuo=map5.cheat()

			print "GAME OVER!"
			exit(0)

#初始化六个地图的实例
Death_map=Death()
Central_corridor_map=CentralCorridor()
Laser_weapon_armony_map=LaserWeaponArmony()
The_bridge_map=TheBridge()
Escape_pod_map=EscapePod()
Cheat_map=Cheat()
#初始化引擎实例，并赋予self.xiansuo='central_corridor'
A_game=Engine('central_corridor')
A_game.play(Death_map,Central_corridor_map,Laser_weapon_armony_map,The_bridge_map,Escape_pod_map,Cheat_map)
