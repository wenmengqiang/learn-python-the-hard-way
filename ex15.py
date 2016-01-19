#encoding:utf-8
from sys import argv
#导入sys模块，并用argv代表sys.argv

script,filename=argv
#将执行时argv变量的内容传递给script和filename

txt=open(filename)
#使用txt的open函数，将filename传递给txt

print "Here's your file %r:"%filename
print txt.read()
#打印出txt.read函数的内容

print "Typen the filename again:"
file_again=raw_input("-->")

txt_again=open(file_again)

#txt_again.close()该函数执行后，下一条指令错误
print txt_again.read()
txt.close()
txt_again.close()

#function —— A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body
#method —— A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self).
#