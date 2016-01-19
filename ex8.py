#encoding:utf-8
formatter="%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %('one','two','three','four')
#在line5，one、two
print formatter %(True,False,True,False)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %("I had this thing.","That you could type up right.","But it didn't sing.","so I said goodnight")
#最后一行有双引号和单引号的原因是，在字符串But it didn't sing中，有单引号