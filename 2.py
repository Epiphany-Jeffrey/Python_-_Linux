class Rectangular():
    #输入一对对角线（与x轴正方向夹脚小于九十度）的两点坐标
    def __init__(self,A1,A2,C1,C2):
        self.A1 = A1
        self.C1 = C1
        self.A2 = A2
        self.C2 = C2
        self.a = C1 - A1
        self.b = C2 - A2
        
    def perimeter(self):
        print(2 * (self.a + self.b))
        
    def area(self):
        print(self.a * self.b)
        
        
a = int(input("请输入第一个矩形的左下角顶点的横坐标："))
b = int(input("请输入第一个矩形的左下角顶点的纵坐标："))
c = int(input("请输入第一个矩形的右上角顶点的横坐标："))
d = int(input("请输入第一个矩形的右上角顶点的纵坐标："))
e = int(input("请输入第二个矩形的左下角顶点的横坐标："))
f = int(input("请输入第二个矩形的左下角顶点的纵坐标："))
g = int(input("请输入第二个矩形的右上角顶点的横坐标："))
h = int(input("请输入第二个矩形的右上角顶点的纵坐标："))

r1 = Rectangular(a,b,c,d)
r2 = Rectangular(e,f,g,h)
r1.perimeter()
r1.area()
r2.perimeter()
r2.area()

#判断是否相交
if r1.C1 > r2.A1 and r1.C2 > r2.A2 and r2.C1 > r1.C1 and r2.C2 > r1.C2:
    r3 = Rectangular(r2.A1,r2.A2,r1.C1,r1.C2)
    r3.perimeter()
    r3.area()
    
elif r2.C1 > r1.A1 and r2.C2 > r1.A2 and r1.C1 > r2.C1 and r1.C2 > r2.C2:
    r4 = Rectangular(r1.A1,r1.A2,r2.C1,r2.C2)
    r4.perimeter()
    r4.area()
    
elif r1.A1 < r2.A1 and r1.A2 > r2.A2 and r1.C1 > r2.C1 and r1.C2 < r2.C2:
    r5 = Rectangular(r2.A1,r1.A2,r2.C1,r1.C2)
    r5.perimeter()
    r5.area()
    
elif r2.A1 < r1.A1 and r2.A2 > r1.A2 and r2.C1 > r1.C1 and r2.C2 < r1.C2:
    r6 = Rectangular(r1.A1,r2.A2,r1.C1,r2.C2)
    r6.perimeter()
    r6.area()

else:
    print("两个矩形不相交")