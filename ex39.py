#encoding:utf-8
#dicts   hashes  这是同一种东西，dictionaries
#为什么index要从0开始，因为他读取的还是二进制，而二进制的第一个数字是0
#create a mapping of state to abbreviation
test={1:'right'}
states = {'Oregon':'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
	}

#create a basic set of states and some cities in them
cities={
	'CA':'San Fracisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
	}

#add some more cities
cities['NY']= 'New York'
cities['OR']='Portland'

#in my own country,some states's abbreviation and its cities
states['HeNan']='YU'
states['ShanXi']='JIN'
cities['YU']='ZhengZhou'
cities['JIN']='DaTong'

#print out some cities
print '-'*10
print "NY State has :",cities['NY']
print "OR State has :",cities['OR']

#print some states
print '-'*10
print "Michigan's abbreviation is",states['Michigan']
print "Florida's abbreviation is:",states['Florida']

#do it by using the state then cities dict
print '-'*10
print "Michigan has:",cities[states['Michigan']]
print "Florida has:",cities[states['Florida']]

#print every state abbreviation  dict.items()函数是否输出该字典中各种对应值
print '-'*10
for state,abbrev in states.items():
	print "%s is abbreviated %s"%(state,abbrev)

#一个函数再次执行，顺序是否一致
print '-'*10
for state,abbrev in states.items():
	print "%s is abbreviated %s"%(state,abbrev)
#两次顺序是一致的，这个顺序是由于print造成还是本身是有序的

#print every city in state
print '-'*10
for abbrev,city in cities.items():
	print "%s has the city %s "%(abbrev,city)

#now do both at the same time
print '-'*10
for  state,abbrev in states.items():
	print "%s state is abbreviated %s and has city %s"%(state,abbrev,cities[abbrev])

print '-'*10
#safely get an abbreviation by state that might not be there
state=states.get('Texas',None)

if not state:
	print "Sorry,no Texas"

#get a city with a default value
city=cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is : %s"%city

#states.keys()的使用
print '-'*10
for state in states.keys():
	print "%s is abbreviated %s "%(state,states[state])

#总结：states.items()函数的功能是返回一个list [('michigan',mi),(Florida,Fl)]
#states.keys()返回的是[Michigan,Florida,HeNan],states.values()返回的是[YU,FL,JIN,NY]

