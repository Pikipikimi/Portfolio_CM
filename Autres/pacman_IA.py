from tkinter import *

# Définir les dimensions du labyrinthe
labyrinthe = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Définir la position initiale de Pac-Man
pacman_x, pacman_y = 1, 1

# Définir la position initiale du fantôme
fantome_x, fantome_y = 3, 7

# Définir la position du point d'arrivée
arrivee_x, arrivee_y = 10, 11

# Définir la direction initiale de Pac-Man
direction = None

# Définir la direction initiale du fantôme
fantome_direction = None

# Définir la fonction d'affichage
def affichage(labyrinthe, pacman_x, pacman_y, fantome_x, fantome_y, arrivee_x, arrivee_y):
    n = len(labyrinthe)
    p = len(labyrinthe[0])
    cnv.delete("all")  # Effacer le contenu précédent du canvas

    for i in range(n):
        for j in range(p):
            x, y = 30 * j, 30 * i
            A, B = (x, y), (x + 30, y + 30)
            if labyrinthe[i][j] == 1:
                cnv.create_rectangle(A, B, fill="blue")
            else:
                cnv.create_rectangle(A, B, fill="black")

    # Dessiner Pac-Man
    x, y = 30 * pacman_y, 30 * pacman_x
    A, B = (x, y), (x + 30, y + 30)
    cnv.create_oval(A, B, fill="yellow")

    # Dessiner le fantôme
    x, y = 30 * fantome_y, 30 * fantome_x
    A, B = (x, y), (x + 30, y + 30)
    cnv.create_oval(A, B, fill="red")

    # Dessiner le point d'arrivée
    x, y = 30 * arrivee_y, 30 * arrivee_x
    A, B = (x, y), (x + 30, y + 30)
    cnv.create_oval(A, B, fill="violet")

# Définir la fonction de déplacement de Pac-Man
def move_pacman(labyrinthe, pacman_x, pacman_y, direction):
    if direction == "RIGHT" and labyrinthe[pacman_x][pacman_y + 1] != 1:
        pacman_y += 1
    elif direction == "LEFT" and labyrinthe[pacman_x][pacman_y - 1] != 1:
        pacman_y -= 1
    elif direction == "UP" and labyrinthe[pacman_x - 1][pacman_y] != 1:
        pacman_x -= 1
    elif direction == "DOWN" and labyrinthe[pacman_x + 1][pacman_y] != 1:
        pacman_x += 1
    return pacman_x, pacman_y

# Définir la fonction de gestion des touches
def on_key_press(event):
    global direction
    if event.keysym == "Right":
        direction = "RIGHT"
    elif event.keysym == "Left":
        direction = "LEFT"
    elif event.keysym == "Up":
        direction = "UP"
    elif event.keysym == "Down":
        direction = "DOWN"

# Définir la fonction de vérification de défaite
def check_defeat(pacman_x, pacman_y, arrivee_x, arrivee_y):
    if pacman_x == fantome_x and pacman_y == fantome_y:
        cnv.create_text(150, 150, text="Défaite !", font=("Helvetica", 32), fill="red")
        master.after(2000, master.destroy)  # Fermer la fenêtre après 2 secondes
        return True
    return False

# Définir la fonction de vérification de la victoire
def check_victory(pacman_x, pacman_y, arrivee_x, arrivee_y):
    if pacman_x == arrivee_x and pacman_y == arrivee_y:
        cnv.create_text(150, 150, text="Victoire !", font=("Helvetica", 32), fill="yellow")
        master.after(2000, master.destroy)  # Fermer la fenêtre après 2 secondes
        return True
    return False

# Initialiser l'affichage
master = Tk()
cnv = Canvas(master, width=30 * len(labyrinthe[0]), height=30 * len(labyrinthe), bg='gray70')
cnv.pack()
affichage(labyrinthe, pacman_x, pacman_y, fantome_x, fantome_y, arrivee_x, arrivee_y)

# Lier les événements clavier
master.bind("<KeyPress>", on_key_press)

# Boucle de jeu
def game_loop():
    global pacman_x, pacman_y, direction
    if direction:
        pacman_x, pacman_y = move_pacman(labyrinthe, pacman_x, pacman_y, direction)
        direction = None  # Réinitialiser la direction après chaque mouvement
        if not check_victory(pacman_x, pacman_y, arrivee_x, arrivee_y):
            affichage(labyrinthe, pacman_x, pacman_y, fantome_x, fantome_y, arrivee_x, arrivee_y)
        if not check_defeat(pacman_x, pacman_y, arrivee_x, arrivee_y):
            affichage(labyrinthe, pacman_x, pacman_y, fantome_x, fantome_y, arrivee_x, arrivee_y)
    master.after(100, game_loop)

# Lancer la boucle de jeu
game_loop()
master.mainloop()