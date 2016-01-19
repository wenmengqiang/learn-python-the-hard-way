#encoding:utf-8
#this one is like your scripts with argv
def print_two(*args):
    arg1,arg2=args
    print "arg1:%s,arg2:%s."%(arg1,arg2)

#ok,that *args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r."%(arg1,arg2)

#this just takes one argument
def print_one(arg):
    print "arg is:%s."%arg
    
#this one takes no arguments
def print_none():
    print "I got nothin'."
    
print_two('zhen','zhen')
print_two_again('wen','mengqiang')
print_one('First!')
print_none()
#运行函数(run)、调用函数(call)、使用函数(use)是同一个意思
#运行函数（run）、调用函数（call）、使用函数（use）是同一个意思
