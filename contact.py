import numpy as np 
from math import sqrt



def contact_ballon(car,ballon,e,C):
    k=0

    pts_proche=999999999999999999

    pts_proches=car.get_contact_points()
    Vecteurs_n=car.get_normal_vectors()
    if ballon.r+ sqrt((car.length**2+car.height**2)/4)>=sqrt((car.x-ballon.x)**2+(car.y-ballon.y)**2):
        pass
    for i in range (len(pts_proches)):
        d= np.square((pts_proches[i][0]-ballon.x)**2+(pts_proches[i][1]-ballon.y)**2)
        
        if d<pts_proche:

            pts_proche=d
            k=i
    if pts_proche<=np.square(ballon.r):

        v_relat=np.array([-car.vx+ballon.vx,-car.vy+ballon.vy])
        v_norm=v_relat/np.linalg.norm(v_relat)
        angle=np.dot(v_norm,Vecteurs_n[k])
        signe=np.sign(v_relat[1])
        angles_depart=car.teta+signe*((np.pi)/2-angle)
        v_direction=np.array([np.cos(angles_depart),np.sin(angles_depart)])
        if k in[0,1,2,3]:
            bras_de_levier=np.abs((car.x-pts_proches[k][0])*v_direction[1]-(car.y-pts_proches[k][1])*v_direction[0])
            if k in [0,2]:
                car.teta_dot-=C*bras_de_levier*np.linalg.norm(ballon.m*v_relat)

            if k in [1,3]:
                car.teta_dot+=C*bras_de_levier*np.linalg.norm(ballon.m*v_relat)

        vcar=np.square(car.vx**2+car.vy**2)
        vballon=np.square(ballon.vx**2+ballon.vy**2)     

        vballon_ap = (ballon.m * vballon + car.m * vcar + car.m * e * (vcar - vballon)) / (car.m + ballon.m)
        
        car.vx= car.vx +(ballon.m * (ballon.vx - car.vx)) / car.m
        car.vy= car.vy +(ballon.m * (ballon.vy - car.vy)) / car.m
        ballon.vx = vballon_ap * v_direction[0]
        ballon.vy = vballon_ap * v_direction[1]

        


        




