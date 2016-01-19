#encoding:utf-8
from sys import argv
from os.path import exists#读取sys.argv变量赋值与argv。读取os.path的exists方法

script,from_file,to_file=argv#将argv赋值与三个变量

print "Copying from %s to %s"%(from_file,to_file)

#we couled do these two on one line too,how?
input=open(from_file)#用open函数打开源文件并将内容赋予input变量
indata=input.read()#indata=(open(from_file).read#用read()将源文件内容赋予indata

print "The input file is %d bytes long"%len(indata)#打印源文件中的长度

print "Does the output file exist? %r"%exists(to_file)#用exists方法检查目标文件是否存在
print "Ready,hit RETURN to continue,CTRL+c to abort."
raw_input()#这个截断很重要，给用户选择的余地

output=open(to_file,'w')#'w'打开目前文件，并将该文件的链接赋予output。难道这里赋予的是内存地址？
output.write(indata)#将该地址内的内容用write()赋予目标文件to_file

print "Alright,all done."

output.close()
input.close()#关闭两个文件，为什么需要在代码中写output.close()，估计是因为内存释放吧