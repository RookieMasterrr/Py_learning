from typing import Any

# :和->都是类型简易符,不强制约束

class stuent:
    # 声明属性,:后面是声明数据类型
    a:Any
    b:Any
    #                o是形参,: object是说明形参类型,可有可无,->bool是说明返回参数类型,可有可无
    def __eq__(self, o: object) -> bool:
        if o.a == self.a and o.b == self.b:
            return True
        else :
            return False

    #                o是形参,: object是说明形参类型,可有可无,->bool是说明返回参数类型,可有可无    
    def __init__(self,A,B) -> None:
        self.a = A
        self.b = B

    def display(self:object) -> None:
        return str(self.a)+" "+str(self.b)

object

s1 = stuent(1,2)
s2 = stuent(1,2)
print(s1.display())
print(s2.display())