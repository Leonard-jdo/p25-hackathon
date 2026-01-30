alpha = 1e-3
beta = 0.8
g = 9,81
class Ballon:

    def __init__(self, x, y, vx, vy,m,r):
        self.x = x
        self.y = y
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

    def corr_contact(self, taille):
        (bord1, bord2, y_sol, y_plafond) = taille
        if self.x + self.r > bord2:#contact à droite
            self.x = bord2 - self.r  
            self.vx = -self.vx * beta 
            
        elif self.x - self.r < bord1:#contact à gauche
            self.x = self.r + bord1               
            self.vx = -self.vx * beta
            
        if self.y - self.r < self.sol:#contact au sol
            self.y = self.r + y_sol               
            self.vy = -self.vy * beta 

        if self.y + self.r > y_plafond:#contact mur 
            self.y = y_plafond - self.r 
            self.vy = -self.vy * beta

    

    
    






    