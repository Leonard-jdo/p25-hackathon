import numpy as np 
from math import sqrt

def contact_ballon(car, ballon, e, C):
    k = 0
    
    pts_proche = float('inf')

    pts_proches = car.get_contact_points()
    
    
    try:
        Vecteurs_n = car.get_normal_vectors()
    except:
        return

  
    dist_centres_sq = (car.x - ballon.x)**2 + (car.y - ballon.y)**2
    rayon_total = ballon.r + sqrt((car.length**2 + car.height**2)/4)
    
    if rayon_total**2 <= dist_centres_sq:
        return

    # 2. Boucle de recherche du point le plus proche
    for i in range(len(pts_proches)):
        # On peut optimiser en n'utilisant pas sqrt ici, mais je garde ta structure
        d = np.sqrt((pts_proches[i][0] - ballon.x)**2 + (pts_proches[i][1] - ballon.y)**2)
        
        if d < pts_proche:
            pts_proche = d
            k = i


    if pts_proche <= ballon.r:

    

        normal = Vecteurs_n[k]
        
       
        vx_rel = ballon.vx - car.vx
        vy_rel = ballon.vy - car.vy
        
      
        vel_along_normal = vx_rel * normal[0] + vy_rel * normal[1]

      
        if vel_along_normal > 0:
            return

        
        j = -(1 + e) * vel_along_normal
        j /= (1 / ballon.m + 1 / car.m)

        
        impulse_x = j * normal[0]
        impulse_y = j * normal[1]

        
        ballon.vx += impulse_x / ballon.m
        ballon.vy += impulse_y / ballon.m
        
        car.vx -= impulse_x / car.m
        car.vy -= impulse_y / car.m

        
        vecteur_contact_x = pts_proches[k][0] - car.x
        vecteur_contact_y = pts_proches[k][1] - car.y
        
        
        tangent_x = -normal[1]
        tangent_y = normal[0]
        
        
        vel_along_tangent = vx_rel * tangent_x + vy_rel * tangent_y
        
        
        cross_product = vecteur_contact_x * tangent_y - vecteur_contact_y * tangent_x
        sens_rot = np.sign(cross_product)
        if sens_rot == 0: sens_rot = 1
            
        
        car.teta_dot += sens_rot * abs(vel_along_tangent) * C * 0.002

        
        penetration = ballon.r - pts_proche
        if penetration > 0:
            
            ballon.x += normal[0] * (penetration + 1.0)
            ballon.y += normal[1] * (penetration + 1.0)