# a = 1
# b = 1
# print(id(a) == id(b)) # 常量池
# a = 2
# print(id(a) == id(b)) # 不可变类型


list1 = [1,2,3]
id2 = id(list1)
list1.append(1)
id1 = id(list1)
print(id1 == id2) # 可变类型