#encoding:utf-8
##animal is-a object(yes,sort of confusing) look at the extra credit
class Animal(object):
	"""docstring for Animal"""
	# def __init__(self, arg):
	# 	super(Animal, self).__init__()
	# 	self.arg = arg
	pass
#定义Dog这个类，由Animal派生
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog, self).__init__()
		self.name = name
#由Animal派生出Cat类
class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self,name):
		super(Cat, self).__init__()
		self.name = name
#定义Person
class Person(object):
	"""docstring for Person"""
	def __init__(self,name):
		super(Person, self).__init__()
		self.name = name

		self.pet=None
#派生
class Employee(Person):
		"""docstring for Employee"""
		def __init__(self, name, salary):
			# super(Employee, self).__init__()
			self.salary = salary
#定义Fish类
class Fish(object):
	"""docstring for Fish"""
	# def __init__(self, arg):
	# 	super(Fish, self).__init__()
	# 	self.arg = arg
	pass
#派生	
class Salmon(Fish):
	"""docstring for Slamon"""
	print "I'm a class,not an object!"
	pass
#派生
class Halibut(Fish):
	"""docstring for Halibut"""
	pass
#初始化rover这个Dog对象
rover=Dog("Rover")
#初始化satan这个Cat对象
satan=Cat("Satan")
							
mary=Person("Mary")

mary.pet=satan

frank=Employee("Frank",12000)

frank.pet=rover

flipper=Fish()

crouse=Salmon

harry=Halibut()

Salmon()
#课外习题一   http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html
#习题二， a class 可以作为 an object 用