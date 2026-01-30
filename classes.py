import numpy as np

dt=0.06
g=9.81
alpha=0.5
m=15
v_h=15 #augmentation de la vitesse quand le mec appuis sur la flèche gauche ou droite au sol
v_saut=10 #vitesse verticale du saut
v_boost=10
demi_h=0.5
demi_l=0.56
k=10

class Car : 
    def __init__(self,x,y,vx,vy,teta,teta_dot,boost,sens_v,sens_h,saut):
        self.x = x
        self.length=10
        self.height=4
        self.y=y
        self.vx=vx
        self.vy=vy
        self.teta=teta   #angle de la voiture
        self.teta_dot=teta_dot #vitesse angulaire
        self.sens_v=sens_v #+-1 (orienté vers le haut/bas dans les airs)
        self.sens_h=sens_h #+-1,0 (gauche/droite)
        self.boost=boost #0 ou 1
        self.saut=saut #0 ou1


    def onsol(self):
        if self.y <= self.height/2 + SOL:
            return True
        return False

    def update(self):
        if self.onsol() and self.saut==False: 
            self.vx=(-alpha*dt/m +1)*self.vx +self.sens_h*v_h + self.boost*v_boost*self.sens_h

        elif self.onsol and self.saut : 
            self.vy=(-g*-alpha/m *self.vy)*dt + self.vy+v_saut #on peut pas sauter et booster en mm temps
            self.vx=(-alpha*dt/m +1)*self.vx +self.sens_h*v_h 
        
        elif self.onsol==False : 
            if self.boost==1:
                self.teta_dot=k
                self.teta=self.teta + self.sens_v*self.teta_dot*dt
                self.vy=-(g+alpha/m*self.vy)*dt + self.vy+ + np.sin(self.teta)*v_boost
                self.vx=self.vx+np.cos(self.teta)*v_boost -alpha*dt/m*self.vx
            else:
                self.vy=-(g+alpha/m*self.vy)*dt + self.vy
                self.vx=self.vx -alpha*dt/m*self.vx

        self.x=self.vx*dt+self.x
        self.y=self.vy*dt+self.y

        




        


         


    

#discrétiqse l'espace et à chaque intstant jhe met à) jour (uodate) à partir de l'accélératiob si le mec boost et qu'il saute l'angle teta impose ou la voiture va aller
#en input j'ai le vecteur de booléen de cez qu'il fait : accélérer, booster, gauche droite
#
