import numpy as np
from math import sqrt

def contact_ballon(car, ballon, e, C):
    """
    e : coefficient de restitution (0 à 1, rebond)
    C : coefficient de transmission de rotation (torque)
    """
    # 1. Optimisation : Test de proximité rapide (Cercle englobant)
    dist_centres = sqrt((car.x - ballon.x)**2 + (car.y - ballon.y)**2)
    # On prend la diagonale de la voiture pour être sûr
    if dist_centres > (ballon.r + max(car.length, car.height)):
        return

    # 2. Trouver le point le plus proche sur le rectangle de la voiture
    # On récupère les points et les normales pré-calculés de la car
    pts_proches = car.get_contact_points()
    vecteurs_n = car.get_normal_vectors()
    
    idx_proche = -1
    min_dist = float('inf')

    for i, pt in enumerate(pts_proches):
        d = sqrt((pt[0] - ballon.x)**2 + (pt[1] - ballon.y)**2)
        if d < min_dist:
            min_dist = d
            idx_proche = i

    # 3. Détection réelle de collision
    if min_dist <= ballon.r:
        # La normale de collision (vecteur pointant de la voiture vers le ballon)
        n = vecteurs_n[idx_proche]
        
        # 4. Calcul des vitesses relatives
        # V_rel = V_ballon - V_voiture
        v_rel = np.array([ballon.vx - car.vx, ballon.vy - car.vy])
        
        # Vitesse relative projetée sur la normale (produit scalaire)
        v_normale_relative = np.dot(v_rel, n)

        # Si v_normale_relative > 0, les objets s'éloignent déjà : on ne fait rien
        if v_normale_relative > 0:
            return

        # 5. Calcul de l'Impulsion (changement de quantité de mouvement)
        # Formule simplifiée de l'impulsion J
        # J = -(1 + e) * v_rel_normale / (1/m_ballon + 1/m_car)
        inv_mass_sum = (1.0 / ballon.m) + (1.0 / car.m)
        j = -(1 + e) * v_normale_relative / inv_mass_sum
        
        impulsion = j * n

        # 6. Mise à jour des vitesses linéaires
        ballon.vx += impulsion[0] / ballon.m
        ballon.vy += impulsion[1] / ballon.m
        
        car.vx -= impulsion[0] / car.m
        car.vy -= impulsion[1] / car.m

        # 7. Rotation de la voiture (Torque)
        # On calcule le bras de levier (vecteur centre_car -> point_impact)
        r_vector = np.array([pts_proches[idx_proche][0] - car.x, 
                             pts_proches[idx_proche][1] - car.y])
        
        # Produit vectoriel 2D pour le couple : rx * fy - ry * fx
        torque = r_vector[0] * (-impulsion[1]) - r_vector[1] * (-impulsion[0])
        car.teta_dot += C * torque / (car.m * 100) # Divisé par inertie simplifiée

        # 8. ANTI-COLLISION (Le secret pour ne pas rester collé)
        # On repousse le ballon pour qu'il ne soit plus à l'intérieur de la car
        overlap = ballon.r - min_dist + 0.1
        ballon.x += n[0] * overlap
        ballon.y += n[1] * overlap