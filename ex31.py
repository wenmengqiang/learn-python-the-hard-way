#encoding:utf-8
print "You enter a dark room with two doors.Do you go through door #1 or door #2?"
door=raw_input("You enter #")

if door=="1":
	print "There is a giant bear here eating a cheese cake.What do you do?"
	print "1.Take the cake."
	print "2.Scream at the bear."

	bear=raw_input(">")

	if bear=="1":
		print "Bear eats your face off.Good job!"
	elif bear=="2":
		print "Bear eats your legs off,Good job!"
	else:
		print "Well ,doing %s is probably better.Bear runs away."%bear

elif door=="2":
	print "You stare into the endless abyss at Cthulhu's retina."	
	print "1,Blueberries."
	print "2.Yellow jackets clothespins."
	print "3.Understanding revolvers yelling melodies."

	insanity=raw_input(">"),

	if insanity=="1" or insanity=="2":
		print "Your body suivives powered by a mind of jello.Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.Good job."

else:
	print "You stumble around and fall on a knife and die.Good job."