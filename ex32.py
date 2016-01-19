#encoding:utf-8
hairs=['brown','blond','red']
eyes=['brown','blue','green']
weights=[1,2,3,4]
sights=['good','normal','bad']

the_count=[1,2,3,4]
fruits=['apples','oranges','pears','aprincots']
changes=[1,'pennies',2,'dimes',3,'quarters']

#this first kind of for_loop go through a list
for number in the_count:
	print "This is count %d"%number

#same as above
for fruit in fruits:
	print "This is %s"%fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in changes:
	print "I got %r"%i

print max(fruits)

#we can also build lists,first start with an empty oranges
element=[]

#then we use range function to do 0 to 5 count
for i in range(0,6):
	print "Adding %d to the list."%i
	#append is a function that lists understand
	element.append(i)

#now we can print them out  too
for i in element:
	print "the # %d element is %d"%(i+1,i)

test=range(1,100)
print test

print test.index(2)
print test.count(100)
test.insert(3,22222)
print test
test.remove(4)
print test
test.reverse()
print test

#list还支持一下操作：test[0],test[-1],test[1:],test[1::1]
#del test[0]
#'+'用来组合列表，'*'用来重复列表
#len(test)   test1+test2   test*3   (3 in test)==True
#cmp(test1,test2)    max(test)   min(test)  list(seq)将元祖转换为列表
#test.count(obj) 统计某个元素出现的次数
#test.extend(seq) 在列表末尾一次追加另一个序列的多个直
#test.index(obj)  从列表中找出某个值第一个匹配想的索引位置
#test.insert(index,obj) 将对象插入列表的某个位置
#test.pop(obj=list[-1])  移除列表中的一个元素，并且返回该元素的值
#test.remove(obj)  移除列表中某个值的第一个匹配项
#test.reverse()  反向列表中的元素
#test.sort([func])  对元列表进行排序