# Laboratoire - CustomTkinter
## Introduction
Le but de ce laboratoire est de créer une interface graphique qui permettra d'afficher une image recadrée prise par la webcam de l'ordinateur.

## Objectifs
- Utiliser la librairie `CustomTkinter` pour créer une interface graphique.
- Utiliser la librairie `opencv-python` pour capturer une image depuis la webcam.
- Comprendre la séparation des composants graphiques et de la logique de l'application.

## Librairies nécessaires
- `pip install customtkinter`
- `pip install opencv-python`
- `pip install pillow`

## Composition de l'interface
### Fenêtre principale
- Un titre.
- Une zone pour afficher les différentes pages (layout).
- Deux boutons pour changer de layout (configuration de la zone / prise d'image).

### Layout Configuration des zones
- Un bouton pour prendre une image.
- L'affichage de l'image prise.
- Un carré sur l'image pour définir la zone de capture.
- (Bonus) Quatre zones de texte pour définir la position et la taille de la zone de capture.

### Layout Prise d'image
- Un bouton pour prendre une image (l'image est rognée à la zone de capture).
- L'affichage de l'image prise.
- Un compteur affichant le nombre d'images prises pour ce layout.

## Aide
### Prise d'image
Pour capturer une image depuis la webcam, nous allons utiliser la librairie `opencv-python`.

Pour capturer une image, nous utiliserons la fonction `cv2.VideoCapture(0)`.
La valeur `0` correspond à l'indice de la webcam. Si vous avez plusieurs webcams, vous pouvez changer la valeur pour utiliser une autre webcam.

Pour afficher une image dans CustomTkinter, il faut utiliser le widget `Label`.

Pour capturer et afficher une image, vous pouvez vous inspirer du code suivant :

```python
import cv2
from PIL import Image
import customtkinter as ctk

# Initialisation de la webcam
camera_index = 0
camera = cv2.VideoCapture(camera_index)

# Capture de l'image
ret, image = camera.read()
if not ret:
    raise RuntimeError("Échec lors de la capture de l'image")

# Conversion de l'image pour l'affichage
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Dessin d'un rectangle
cv2.rectangle(image_rgb, (10, 10), (100, 200), (0, 255, 0), 3)
photo = ctk.CTkImage(Image.fromarray(image_rgb), size=(width, height))

# Affichage de l'image
root = ctk.CTk()  # Assuming 'root' is your main window
label = ctk.CTkLabel(root, image=photo, text="")
label.pack()

# Libération de la webcam
camera.release()
