#encoding:utf-8
def cheese_and_crackers(cheese_count,boxes_of_crackers):#定义函数
    print "You have %d cheese!"%cheese_count#打印cheese数量
    print "You have %d boxes of crackers!"%boxes_of_crackers#打印crackers数量
    print "Man,that's enough for a party!"
    print "Get a blanket.\n"#换行
    
print "We can just give the functiongs numbers directly:"
cheese_and_crackers(20,30)#直接传参调用函数

print "OR,we can use variable from our script:"
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)#使用变量传参

print "We can even do math inside too:"
cheese_and_crackers(10+5,5+6)#使用表达式传递参数

print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+200)#使用结合变量的表达式传参
