# is id() hash()

# hash value is based on object's value


class stuent:
    # __slots__=("a","b")

    #                o是形参,: object是说明形参类型,可有可无,->bool是说明返回参数类型,可有可无
    a:int
    b:int
    def __eq__(self, o: object) -> bool:
        if o.a == self.a and o.b == self.b:
            return True
        else :
            return False
    
    def __init__(self,A,B) -> None:
        self.a = A
        self.b = B

s1 = stuent(1,2)
s2 = stuent(1,2)

# ==默认是使用object.__eq__,所以默认是比较两个实例的内存地址,所以一般不会相等
# 但是我这里重载了
print(s1 == s2)

# print(stuent.__dict__)
print(s1.__setattr__("a",12))
print(s1.__dict__)