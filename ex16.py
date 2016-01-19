#encoding:utf-8
# clos=关闭文件。跟你编辑器的 文件->保存，一个意思
# read=读取文件内容，你可以把结果赋给一个变量
# readline=读取文本文件中的一件
# truncate=清空文件，请小心使用该命令
# write(stuff)=将stuff写入文件
from sys import argv

script,filename=argv

print "We're going to erase %r."%filename
print "If you don't want that,hit ctrl+c(^c)."
print "If you do want that,hit return."#这个区块的目的是提示用户进行清除文件内容的操作

raw_input("?")#提示符

print "Opening the file..."
target=open(filename,'w')#打开文件

print "Truncating the file.Goodbye!"
target.truncate()#清空target里的所有内容，并写入ex.txt

print "Now I'm going to ask you for three lines."#提示用户输入三行文字

line1=raw_input("line1: ")#提示输入line1的文字，赋予变量line1，下两行同
line2=raw_input("line2: ")
line3=raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1+"\n"+line2+"\n"+line3+"\n")
# target.write(line1)#把line1内容写入target，下同
# target.write("\n")#在target里面换行，下同
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally,we close it."
target.close()#在cmd中关闭target变量

