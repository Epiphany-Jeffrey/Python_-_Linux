class Fan():
    '''模拟一个风扇'''

    def __init__(self,sp,ra,co,bo):
        SLOW = 1
        MEDIUM = 2
        FAST = 3
        
        self.speed = sp
        self.radius = ra
        self.color = co
        self.open = bo
        
    def speed(self):
        if self.speed == "fast":
            self.speed = 3
        if self.speed == "medium":
            self.speed = 2
        if self.speed == "slow":
            self.speed = 1
    
    def start_set(self):
        self.speed = 1
        self.radius = 5
        self.color = "blue"
        self.open = False
        
        
f1 = Fan("fast",10,"yellow",True)
f2 = Fan("medium",5,"blue",False)

print(f1.speed,f1.radius,f1.color,f1.open)
print(f2.speed,f2.radius,f2.color,f2.open)