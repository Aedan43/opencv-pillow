
import numpy as np
import cv2 as cv

def rien(x):
    pass

# Créer une image noire et une fenêtre
img = np.zeros((300, 512, 3), np.uint8)

cv.namedWindow('image')

# Créer des barres de piste pour le changement de couleur
cv.createTrackbar('R', 'image', 0, 255, rien)
cv.createTrackbar('G', 'image', 0, 255, rien)
cv.createTrackbar('B', 'image', 0, 255, rien)

# Créer un commutateur pour la fonctionnalité ON/OFF
switch = '0 : OFF \n1 : ON'

cv.createTrackbar(switch, 'image', 0, 1, rien)

while True:
    cv.imshow('image', img)

    k = cv.waitKey(1) & 0xFF

    if k == 27:
        break

    # Obtenir les positions actuelles des quatre trackbars
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')

    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()


