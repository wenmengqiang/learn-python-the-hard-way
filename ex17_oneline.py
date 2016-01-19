#encoding:utf-8
from sys import argv
from os.path import exists#读取sys.argv变量赋值与argv。读取os.path的exists方法

script,from_file,to_file=argv#将argv赋值与三个变量
print "Does the fromfile and in file exist? %r"%((exists(to_file))and(exists(from_file)))
(open(to_file,'w')).write((open(from_file).read()))
print "All done!"
#我也用一行完成了这个脚本