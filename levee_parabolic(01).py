import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Données du problème
# -----------------------------
h = 20                  # levée maximale (mm)
beta_lift = 120         # angle de levée (°)
beta_dwell = 40         # maintien haut (°)
beta_return = 120       # angle de descente (°)

# Angles clés
theta_lift_end = 120
theta_dwell_end = 160
theta_return_end = 280

# Subdivision
n = 19
dtheta = 360 / n
theta = np.arange(0, 360 + dtheta, dtheta)

# Coefficient parabolique
k = 2 * h / beta_lift**2

# -----------------------------
# Calcul de la levée
# -----------------------------
y = []

for t in theta:
    if 0 <= t <= theta_lift_end:
        # Levée parabolique
        if t <= beta_lift / 2:
            y_t = k * t**2
        else:
            y_t = h - k * (beta_lift - t)**2

    elif theta_lift_end < t <= theta_dwell_end:
        # Palier haut
        y_t = h

    elif theta_dwell_end < t <= theta_return_end:
        # Descente parabolique symétrique
        t_r = t - theta_dwell_end  # angle relatif descente
        if t_r <= beta_return / 2:
            y_t = h - k * t_r**2
        else:
            y_t = k * (beta_return - t_r)**2

    else:
        # Palier bas
        y_t = 0

    y.append(y_t)

y = np.array(y)

# -----------------------------
# Affichage du tableau
# -----------------------------
print(" Angle (°)   Levée y (mm)")
print("---------------------------")
for angle, lev in zip(theta, y):
    print(f"{angle:8.2f}   {lev:8.3f}")

# -----------------------------
# Tracé graphique
# -----------------------------
plt.figure(figsize=(9, 5))
plt.plot(theta, y, marker='o', linewidth=2)
plt.xlabel("Angle de rotation θ (°)")
plt.ylabel("Levée y (mm)")
plt.title("Loi parabolique – subdivision 360° / 19")
plt.grid(True)
plt.xlim(0, 360)
plt.ylim(0, h * 1.1)
plt.show()
