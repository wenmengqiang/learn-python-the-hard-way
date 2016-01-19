#encoding:utf-8
from sys import argv

script,user_name,user_gender=argv
prompt='<Type here-->'

if(user_gender=='male'):
    print "Hi %s,I'm the %s man."%(user_name,script)
    print "I'd like to ask you a few question."
    print "Do you like to answer me %s?"%user_name
    do_like=raw_input(prompt)
else:
    print "Hi %s,I'm the %s woman."%(user_name,script)
    print "I'd like to ask you a few question."
    print "Do you like to answer me %s?"
    do_like=raw_input(prompt)

print "Where do you live %s"%user_name
lives=raw_input(prompt)

print "What kind of computer do you have?"
computer=raw_input(prompt)

print """
Alright,so you said %r about liking to answer me.
You live in %r,no sure where that is.
And you have a %r computer.Nice.
"""%(do_like,lives,computer)