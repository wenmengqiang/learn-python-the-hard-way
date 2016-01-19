#encoding:utf-8
#总共有100辆车
cars =100
#每辆车可以坐四个人
space_in_a_car=4.0  #If there are 2.8 people average in each cars,we got 2,that's a waste.
#总共有30个司机
drivers=30
#目前有90个乘客待送
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

print "There are ",cars,"cars available."
print "There are only ",drivers," drivers available."
print "There will be ",cars_not_driven," empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have ",passengers,"peopel to carpool today."
print "We need to put",average_passengers_per_car,"people in each car."

#python作为计算器
i=199
x=31
j=x*x/i-i
print "We got j =",j