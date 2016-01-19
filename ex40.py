#encoding:utf-8
# class MyStuff(object):
# 	def __init__(self):
# 		self.tangerine="And now a thousand years between"

# 	def apple(self):
# 		print "I AM CLASSY APPLES!"

# thing=MyStuff()
# thing.apple()
# print thing.tangerine

cities={'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'
	}
cities['NY']='New York'
cities['OR']='Portland'

def find_city(themap,state):
	if state in themap:
		return themap[state]
	else:
		return "Not Found!"

#ok pay attention!
cities['_find']=find_city

while True:
	print "state? (ENTER to quit)",
	state=raw_input("->")
	if not state:break

#this line is the most important ever !study!
	city_found=cities['_find'](cities,state)
	print city_found


##############  find the key line,read it ,and then read it backwards ,and then read it  inside-out
##############  the 2nd edition,this excersece is very important
##############  front to back     back to  front    counter-clock-wise