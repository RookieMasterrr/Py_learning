list1 = [1,2,3]
list2 = [1,2,3]
# 基本类型,==比较的是values
print(list1==list2)

# is和id比较的一样,都是identity,内存地址
print(list1 is list2)
print(id(list1)==id(list2))

# 1和1.0在常量池中的地址一定不一样
print(1 is 1.0)
