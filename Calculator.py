class Calculator():
    #相加
    def add(self,a,b):
        return a+b
    #相除
    def div(self,a,b):
        if b==0:
            return "除数不能为0"
        else:
            return a/b

    #相乘
    def mul(self,a,b):
        return a*b

    #相减
    def sub(self,a,b):
        return a-b