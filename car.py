import numpy as np
from constantes import SOL, BORD1, BORD2, PLAFOND, dt, alpha, g, v_h, v_saut, v_boost, k
from math import cos, sin
from input import inputs

class Car: 
    def __init__(self, x=500, y=300, vx=0, vy=0, teta=0, teta_dot=0):
        self.m = 15
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.length = 100
        self.height = 50
        self.teta = teta   # Angle en radians
        self.teta_dot = teta_dot # Vitesse angulaire
        
        # Inputs
        self.fleche_gauche = False
        self.fleche_droite = False
        self.fleche_bas = False
        self.fleche_haut = False
        self.boost_bool = False
        self.saut = False

    def get_inputs(self):
        self.fleche_gauche, self.fleche_droite, self.fleche_bas, self.fleche_haut, self.saut, self.boost_bool, a = inputs()

    def sens_v(self):  # Gauche / Droite
        if self.fleche_gauche:
            return -1
        elif self.fleche_droite:
            return 1
        return 0
    
    def sens_h(self): # Bas / Haut (Rotation)
        if self.fleche_bas:
            return 1
        elif self.fleche_haut:
            return -1
        return 0
    
    def boost(self):
        if self.boost_bool:
            return 1
        return 0

    def onsol(self):
        # Correction : Y augmente vers le bas. On est au sol si le bas de la voiture dépasse la ligne SOL.
        return self.y + self.height/2 >= SOL

    def update(self):
        self.get_inputs()
        
        # Initialisation des accélérations
        ax = 0
        ay = 0

        # 1. Gravité (Toujours active vers le bas, donc positif en Pygame)
        # On multiplie par 50 pour que l'effet soit visible à l'écran
        ay += g * 100 

        # 2. Frottements (S'opposent à la vitesse)
        ax += -alpha * self.vx
        ay += -alpha * self.vy

        # 3. Gestion Sol vs Air
        if self.onsol():
            # Correction de position pour ne pas s'enfoncer
            self.y = SOL - self.height/2
            
            # Annulation de la vitesse verticale si on tombe
            if self.vy > 0:
                self.vy = 0
            
            # La réaction du sol annule la gravité
            ay -= g * 50 

            # Déplacement au sol (Moteur)
            # On utilise sens_v() comme dans votre fichier original
            ax += self.sens_v() * v_h * 50

            # Saut (Impulsion vers le HAUT, donc négatif)
            if self.saut:
                self.vy = -v_saut * 80 
                self.y -= 5 # Petite impulsion pour décoller du sol

        else:
            # En l'air : Rotation et Boost
            
            # Rotation via sens_h (Haut/Bas)
            dir_rot = self.sens_h()
            if dir_rot != 0:
                self.teta_dot = dir_rot * k * 0.5
            else:
                self.teta_dot = 0 # Stabilisation
            
            self.teta += self.teta_dot * dt

            # Boost
            if self.boost() == 1:
                poussee = v_boost * 100
                ax += cos(self.teta) * poussee
                ay += sin(self.teta) * poussee

        # 4. Intégration (Euler) : Vitesse += Accélération * dt
        self.vx += ax * dt
        self.vy += ay * dt
        
        # Position += Vitesse * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

        # 5. Vérification des murs
        self.contact_mur()

    def contact_mur(self):
        # Mur Gauche
        if self.x - self.length/2 < BORD1:
            self.x = BORD1 + self.length/2
            self.vx = -self.vx * 0.5 # Rebond avec perte d'énergie
        
        # Mur Droit
        elif self.x + self.length/2 > BORD2:
            self.x = BORD2 - self.length/2
            self.vx = -self.vx * 0.5

        # Plafond (Sécurité)
        if self.y - self.height/2 < 0:
            self.y = self.height/2
            self.vy = -self.vy * 0.5

    def get_contact_points(self):
        contact_points = []
        x = self.x
        y = self.y
        theta = self.teta
        L = self.length
        h = self.height

        # Les 8 points autour de la voiture
        a = [(1,1),(1,-1),(-1,-1),(-1,1),(0,1),(1,0),(0,-1),(-1,0)]

        for pt in a:
            # Formule de rotation vectorielle
            val_x = x + pt[0] * (L/2) * cos(theta) - pt[1] * (h/2) * sin(theta)
            val_y = y + pt[0] * (L/2) * sin(theta) + pt[1] * (h/2) * cos(theta)
            contact_points.append(np.array([val_x, val_y]))
            
        return contact_points

    def get_normal_vectors(self):
        normal_vectors = []
        pos = np.array([self.x, self.y])
        
        for contactpoint in self.get_contact_points():
            vector = contactpoint - pos
            norm = np.linalg.norm(vector)
            if norm == 0: norm = 1
            normal_vectors.append(vector/norm)

        return normal_vectors