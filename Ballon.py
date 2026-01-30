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
        dt = 0.2 #implémentation méthode d'Euler 
        ax = (-alpha * self.vx) / self.m #frottements fluides uniquement
        ay = ((-alpha * self.vy) / self.m) + g  
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.corr_contact()

    def corr_contact(self, taille):
        (x_lim, y_lim) = taille
        if self.x + self.r > x_lim:#contact à droite
            self.x = x_lim - self.r  
            self.vx = -self.vx 
            
        elif self.x - self.r < 0:#contact à gauche
            self.x = self.r                
            self.vx = -self.vx 
            
        if self.y - self.r < 0:#contact au sol
            self.y = self.r               
            self.vy = -self.vy 

        if self.y + self.r > y_lim:#contact mur 
            self.y = y_lim - self.r 
            self.vy = -self.vy 

    

    
    






    