#encoding:utf-8
# my_name="WenMengqiang"
# my_age=29 #not a lie
# my_height=173 #cm
# my_weight=85 #kg
# my_eyes='black'
# my_teeth='yellow'
# my_hair='black'
# print "Let's talk about %s."%my_name
# print "His age is %d."%my_age
# print "He is %d cm tall."%my_height
# print "He is %d kg heavy."%my_weight
# print "Actually that's too heavy."
# print "He's got %s eyes and %s hair."%(my_eyes,my_hair)
# print "His teeth are usually %s depending on coffeee."%my_teeth

# #This line is very tricky,try to get it exactly right.
# print "If I add %d,%d and %d,I get %d"%(my_age,my_height,my_weight,my_age+my_height+my_weight)

name="WenMengqiang"
age=29 #not a lie
height=173.0 #cm
weight=85 #kg
eyes='black'
teeth='yellow'
hair='black'
print "Let's talk about %s."%name
print "His age is %d."%age
print "He is %f inch tall."%(height*0.3937)
print "He is %f p heavy."%(weight*2.2046)
print "Actually that's too heavy."
print "He's got %s eyes and %s hair."%(eyes,hair)
print "His teeth are usually %s depending on coffeee."%teeth

#This line is very tricky,try to get it exactly right.
print "If I add %r,%r and %r,I get %r."%(age,height,weight,age+height+weight)

# 'd'	返回要格式化对象的十进制表示，如果可以
# 'i'	返回要格式化对象的十进制表示，如果可以
# 'o'	返回要格式化对象的八进制表示，如果可以
# 'u'	同格式化符'd'
# 'x'	返回要格式化对象的十六进制表示，如果可以【如果要求的前导，使用'0x'】
# 'X'	返回要格式化对象的十六进制表示，如果可以【如果要求的前导，使用'0X'】
# 'e'	返回要格式化对象的浮点的科学计数的表示，如果可以【使用'e'】
# 'E'	返回要格式化对象的浮点的科学计数的表示，如果可以【使用'E'】
# 'f'	返回要格式化对象的浮点数表示，如果可以
# 'F'	返回要格式化对象的浮点数表示，如果可以
# 'g'	使用小写字母科学计数格式，如果指数小于-4或不少于精度,否则返回十进制格式。
# 'G'	使用大写字母科学计数格式，如果指数小于-4或不少于精度,否则返回十进制格式。
# 'c'	对0-255之间的整数返回其对应的ASCII码字符（其它整数报错），或者返回单个字符本身
# 'r'	返回要格式化对象的__repr__()方法的返回值
# 's'	返回要格式化对象的__str__()方法的返回值
# '%'	即每两个%显示一个