# 为什么可变对象不可Hash
# 这里的Hash应该是(values到identity,数值到地址的映射,而可变对象更改的时候,value变了,但是identity没变,两个key(value)对应一个value(identity),发生了冲突!)

a = 1
b = 1
print(a is b)
print(hash(a))
# hash(a)的数值是根据a.__hash__()算出来的

c = 1.1
d = 1.1
print(c is d)

e = "abcde"
f = "abcde"
print(e is f)

tuple1 = (1,2,3)
tuple2 = (1,2,3)
print(tuple1 is tuple2)
# print(hash(tuple1))
# print(hash(tuple2))

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)

dic1 = {1:1,2:2}
dic2 = {1:1,2:2}
print(dic1 is dic2)

# d = 