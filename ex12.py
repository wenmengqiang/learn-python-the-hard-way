#encoding:utf-8
age=raw_input("How old are you?")
height=raw_input("How tall are you?")
weight=raw_input("How much dou you weigh?")
#print "So you're %r old,%s tall,%s weigh."%(age,height,weight)
#cmd下的输出在6'7"这里没有使用单引号，甚至84kg这里也没有单引号，难道是因为格式化为%s？
print "So you're %r old,%r tall,%rweigh."%(age,height,weight)
#终于搞明白上一节为什么会输出为'6\'7"了，原来格式化为%r，这种情况下，必须有\才能正常输出
#python -m pydoc raw_input，其中pydoc是python的帮助文档，用来查询raw_input命令是怎么用
#看完了，确实看不懂，os命令大概知道一点，用户是在nt内核或者posix内核中调用什么东西
#python -m pydoc open****the preferred way
#python -m pydoc file****使用方法貌似和open命令一样,(name[.mode[.buffering])->file object
#python -m pydoc os**********help on module os
#os模块的内容分为这几个，第一级别是classes、functions，在classes下有  exception、error、method、data descriptor
#class stat_result
#import os from  os.path import join,getsize
#python -m pydoc sys   ******help on module sys
#dynamic objects、static objects、functions、DATA
