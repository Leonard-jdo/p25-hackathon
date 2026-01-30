class Ballon:

    def __init__(self, x, y, vx, vy,m,r):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m

    def is_on_floor(self):
        if self.x == 0:
            return True 
        else : 
            return False
        
    def is_contact(self, angle):
        if 
    
    def gravity_without_contact(self,alpha,g):
        dt = 0.2 #implémentation méthode d'Euler 
        ax = (-alpha * self.vx) / self.m #frottements fluides uniquement
        ay = ((-alpha * self.vy) / self.m) + g  
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.y <= 0:
            self.y = 0
            self.vy = -self.vy * 0.8  
    






    