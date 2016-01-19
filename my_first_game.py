#encoding:utf-8
def start():
	print "You stand in front of a hole which searched for three days."
	print "It's deep,you throw a stone in it,reflecting nothing."
	print "You will go in it, do you?"
	
	next=raw_input("y or n->")

	if next=="y":
		path()

	else:
		print "After several days' searching,I'm tired and wanna go away!!!!!\t Just go away!!"

def path():
	print "You walk a mile away in the hole,just listening your heartbeat!"
	print "You come to a fork road,chose one!"
	
	next=raw_input("l or r or m->")

	if next=="l":
		treasure()

	elif next=="m":
		magic()

	else:
		dead()

def treasure():
	print "You see a lot of gold in a pool ,the pool is full of blood and bones from human and other stuff you don't know. "
	print "Will you follow?"

	next=raw_input("y or n ->")

	if next=="y":
		print "You are blinded by gold,going into the pool leads to the death."

	else:
		print "You just go back to the fork road."
		path()

def magic():
	print "In the end of this way,there is a box with a light!"
	print "You open it,then you see a delicate staff.There is a line of word on it ."
	print "The man who wave this staff,will have the power to ruin a mountain in a second.At the mean time,he will become sicker and sicker by using this power."
	print "You have to decide whether you take it."

	next=raw_input("y or n->")

	if next=="y":
		print "You become a famous wizard take the staff home.but you know you will die soon,and you are addicted to gorgers and money."
		print "A years later,you die."

	else:
		print "You are smart enough to go back to the fork road."
		dead()

def dead():
		print "You walk so long that you forget when and where you are."
		print "Finally,you walk out."	

start()