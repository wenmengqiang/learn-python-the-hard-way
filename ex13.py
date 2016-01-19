#encoding:utf-8
from sys import argv

script,x=argv

# print "The script is called :",script
# print "Your first variable is: ",first
# print "Your second variable is:",second
# print "Your third variable is:",third
# #need more than 2 values to unpack 参数数量不足
#少量参数
# script,x,y=argv
# print "The script is called:",script
# print "The script is located in:",(x,y)
#大量参数
# script,big,colour,weight,is_zhinengji,os_type=argv
# print "The script is called:",script
# print "Your favourite phone is:",(big,colour,weight,is_zhinengji,os_type)
#将raw_input与argv一起使用
print "The script is called:",script
print "What you want is:",raw_input(x)
