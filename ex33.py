#encoding:utf-8
def while_loop(j):
	numbers=[]
	i=0
	while i<j:
		print "At the top i is %d"%i
		numbers.append(i)

		i+=1
		print "numbers now:",numbers
		print "At the bottom i is %d"%i

		print "The numbers: "

	for num in numbers:
		print num
while_loop(7)
