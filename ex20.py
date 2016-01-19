#encoding:utf-8
from sys import argv

script,input_file=argv#将argv赋值与script,input_file

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count,f):
    print line_count,f.readline()#readline()第一次接触
    
current_file=open(input_file)

print "First,let's print the whole file:\n"

print_all(current_file)#该函数执行后，文件的IO指针已经到达文件末尾

print "\nNow ,let's rewind,kind of like a tape."

rewind(current_file)#该函数执行后，文件的IO指针重头开始

print "\nLet's print three lines:"

current_line=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)
