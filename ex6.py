#encoding:utf-8
x="There are %d types of peopel."%10
#定义字符串变量x，将10以%d方式输出
binary="binary"
do_not="don't"
#定义字符串变量binary和do_not
y="Those who know %s and those who %s."%(binary,do_not)
#使用binary和do_not定义字符串变量y

print x
print y
#打印以上两个变量

print "I said:%r"%x
print "I also said:%r."%y
#用%r的格式输出以上两个变量

hilarious=False
joke_evaluation="Isn't that joke funny?!%r"
#定义两个变量hilarious和joke_evaluation

print joke_evaluation%hilarious
#把变量joke_evaluation中的格式化字符用hilarious打印出

w="This is the left side of ..."
a="a string with the right side."
#定义字符串变量w和a

print w+a
#使用加号连接w和a联合输出
#因为+作为操作符，可以将两个字符串变量连接后输出