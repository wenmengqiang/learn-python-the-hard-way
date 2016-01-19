#encoding:utf-8
from sys import argv

script,filename=argv

print "Read from ex.txt"
target=open(filename)
print target.read()

target.close()