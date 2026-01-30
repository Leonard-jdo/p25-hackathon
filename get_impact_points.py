import numpy as np
from car import car

# fonctions qui renvoient une liste des coordonnées des 8 points d'impact de la voiture ainsi que les coordonnées des vecteutrs normaux
def get_contact_points(self):

    contact_points = []
    x = self.x
    y = self.y
    theta = self.theta
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
    pos = np.array(x,y)
    theta = self.theta
    L = self.length
    h = self.height

    for contactpoint in get_contact_points():
        vector = contactpoint - pos
        normal_vectors.append(vector/np.linalg.norm(vector))

    return normal_vectors