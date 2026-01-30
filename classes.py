import numpy as np

dt=0.06
g=9.81
alpha=0.5
v_h=15 #augmentation de la vitesse quand le mec appuis sur la flèche gauche ou droite au sol
v_saut=10 #vitesse verticale du saut
v_boost=10
demi_h=0.5
demi_l=0.56
k=10

class Car : 
    def __init__(self,x,y,vx,vy,teta,teta_dot,b_boost,fleche_gauche,fleche_droite,fleche_bas,fleche_haut,b_saut):
        self.m=15
        self.x = x
        self.length=10
        self.height=4
        self.y=y
        self.vx=vx
        self.vy=vy
        self.teta=teta   #angle de la voiture
        self.teta_dot=teta_dot #vitesse angulaire
        self.fleche_gauche=fleche_gauche
        self.fleche_droite=fleche_droite
        self.fleche_bas=fleche_bas
        self.fleche_haut=fleche_haut
        self.boost=b_boost
        self.saut=b_saut

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
        if self.boost==True:
            return 1
        return 0

    def onsol(self):
            if self.y==0:
                return True
            return False

    def update(self):
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


        
