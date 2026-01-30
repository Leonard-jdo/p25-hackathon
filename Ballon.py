BORD1, BORD2 = 0, 1320
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
        self.y = SOL
        self.vx = vx
        self.vy = vy
        self.m = m
        self.r = r
        self.BUT_BAS = 40
        self.BUT_HAUT = 400
    
    def reset_position(self):
        self.x = (BORD1+BORD2)/2
        self.y = SOL
        self.vx = 0
        self.vy = 0

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
        marge = 1 # Petite marge pour éviter de rester collé

        # --- MUR DROIT ET BUT DROIT ---
        if self.x + self.r >= BORD2:
            # Si on est dans la zone du but
            if self.BUT_BAS <= self.y <= self.BUT_HAUT:
                if self.x > BORD2:
                    return "GOAL_RIGHT"
                # Optionnel : si tu veux que ça rebondisse quand même 
                # tant que le centre n'a pas traversé :
                # self.x = BORD2 - self.r - marge
                # self.vx = -self.vx * beta
            else:
                # Rebond sur le mur (on ajoute -marge pour décoller du mur)
                self.x = BORD2 - self.r - marge  
                self.vx = -self.vx * beta

        # --- MUR GAUCHE ET BUT GAUCHE ---
        elif self.x - self.r <= BORD1:
            if self.BUT_BAS <= self.y <= self.BUT_HAUT:
                if self.x < BORD1:
                    return "GOAL_LEFT"
            else:
                self.x = BORD1 + self.r + marge # On décolle vers la droite
                self.vx = -self.vx * beta

        # --- SOL ---
        if self.y - self.r <= SOL:
            self.y = SOL + self.r + marge
            self.vy = -self.vy * beta 

        # --- PLAFOND ---
        if self.y + self.r >= PLAFOND:
            self.y = PLAFOND - self.r - marge
            self.vy = -self.vy * beta
        
        return None

    

    
    






    