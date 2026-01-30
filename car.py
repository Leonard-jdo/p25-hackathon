import numpy as np
from constantes import SOL, BORD1, BORD2, PLAFOND,dt,alpha,g
from math import cos
from input import inputs


v_h=15 #augmentation de la vitesse quand le mec appuis sur la flèche gauche ou droite au sol
v_saut=10 #vitesse verticale du saut
v_boost=10
demi_h=0.1
demi_l=0.4
k=10

def to_pi_minuspi(x):
    return x

class Car: 
    def __init__(self,x=500,y=90,vx=0,vy=0,teta=0,teta_dot=0):
        self.m = 15
        self.x = x
        self.length=10
        self.height=4
        self.y=y
        self.vx=vx
        self.vy=vy
        self.teta=teta   #angle de la voiture
        self.teta_dot=teta_dot #vitesse angulaire
        self.fleche_gauche=False
        self.fleche_droite=False
        self.fleche_bas=False
        self.fleche_haut=False
        self.boost_bool = False
        self.saut=False


    def get_inputs(self):
        self.fleche_gauche, self.fleche_droite, self.fleche_bas, self.fleche_haut, self.saut, self.boost_bool, a = inputs()

    def sens_v(self) :  #+-1,0 (gauche/droite)
        if self.fleche_gauche==True:
            return -1
        elif self.fleche_droite==True:
            return 1
        return 0
    
    def sens_h(self) : #+-1,0 (bas/haut)
        if self.fleche_bas==True:
            return -1
        elif self.fleche_haut==True:
            return 1
        return 0
    
    def boost(self):
        if self.boost_bool==True:
            return 1
        return 0

    def onsol(self):
        if self.y <= self.height/2 + SOL+3:
            return True
        return False

    def update(self):
        self.get_inputs()
        if self.onsol() and self.saut==False: 
            self.vx=(-alpha*dt/self.m +1)*self.vx +self.sens_h()*v_h + self.boost()*v_boost*self.sens_h()

        elif self.onsol() and self.saut : 
            self.vy=(-g*-alpha/self.m *self.vy)*dt + self.vy+v_saut #on peut pas sauter et booster en mm temps
            self.vx=(-alpha*dt/self.m +1)*self.vx +self.sens_h()*v_h 
        
        elif not self.onsol() : 
            if self.boost()==1:
                self.teta_dot=k
                self.teta=self.teta + self.sens_v()*self.teta_dot*dt
                self.vy=-(g+alpha/self.m*self.vy)*dt + self.vy+ + np.sin(self.teta)*v_boost
                self.vx=self.vx+np.cos(self.teta)*v_boost -alpha*dt/self.m*self.vx
            else:
                self.vy=-(g+alpha/self.m*self.vy)*dt + self.vy
                self.vx=self.vx -alpha*dt/self.m*self.vx

        self.x=self.vx*dt+self.x
        self.y=self.vy*dt+self.y


    def get_contact_points(self):
        contact_points = []
        x = self.x
        y = self.y
        theta = self.teta
        L = self.length
        h = self.height

        a = [(1,1),(1,-1),(-1,-1),(-1,1),(0,1),(1,0),(0,-1),(-1,0)]

        for pt in a:
            contactpoint = np.array([x + pt[0] * (L/2) * np.cos(theta) - pt[1] * (h/2) * np.sin(theta), y + pt[0] * (L/2) * np.sin(theta) + pt[1] * (h/2) * np.cos(theta)])
            contact_points.append(contactpoint)
        return(contact_points)


    def get_normal_vectors(self):

        normal_vectors=[]
        x = self.x
        y = self.y
        pos = np.array([x,y])
        L = self.length

        for contactpoint in self.get_contact_points():
            vector = contactpoint - pos
            normal_vectors.append(vector/np.linalg.norm(vector))

        return normal_vectors

        
    def contact_mur(self):
        if self.x - (self.length/2)*abs(cos(self.teta)) <= BORD1:
            self.x = 0
            self.vx = -0.2*self.vx
            self.vy = 0.5*self.vy

            theta = to_pi_minuspi(self.teta)
            if theta > 0 :
                self.teta_dot += 1
            elif theta < 0:
                self.teta_dot -= 1


        if self.x + (self.length/2)*abs(cos(self.teta)) >= BORD2:
            self.x = 0
            self.vx = -0.2*self.vx
            self.vy = 0.5*self.vy

            theta = to_pi_minuspi(self.teta)
            if theta > 0 :
                self.teta_dot += 1
            elif theta < 0:
                self.teta_dot -= 1