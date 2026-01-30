BORD1, BORD2 = 75, 1320
PLAFOND = 690
SOL = 90
dt = 0.06
bord1 = 10
bord2 = 1780
plafond = 500
sol = 10

beta = 0.8

class Ballon:

    def __init__(self, vx, vy,m,r):
        self.x = (BORD1+BORD2)/2
        self.y = SOL + r
        self.vx = vx
        self.vy = vy
        self.m = m
        self.r = r

    def is_on_floor(self):
        if self.y <= self.r:
            return True 
        else : 
            return False
    
    def gravity_without_contact(self,alpha,g):
        ax = (-alpha * self.vx) / self.m #frottements fluides uniquement
        ay = ((-alpha * self.vy) / self.m) + g  
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.corr_contact()

    def corr_contact(self):
        if self.x + self.r >= BORD2:#contact à droite
            self.x = BORD2 - self.r  
            self.vx = -self.vx * beta 
            
        elif self.x - self.r <= BORD1:#contact à gauche
            self.x = self.r + BORD1               
            self.vx = -self.vx * beta
            
        if self.y - self.r <= SOL:#contact au sol
            self.y = self.r + SOL               
            self.vy = -self.vy * beta 

        if self.y + self.r >= PLAFOND:#contact mur 
            self.y = PLAFOND - self.r 
            self.vy = -self.vy * beta

    

    
    






    