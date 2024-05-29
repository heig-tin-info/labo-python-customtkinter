# Laboratoire - CustomTkinter
## Introduction
Le but de ce laboratoire est de créer une interface graphique qui va permettre d'afficher 
une image recadrée prise par la webcam de l'ordinateur.

## Buts
- Utiliser la librairie `CustomTkinter` pour créer une interface graphique.
- Utiliser la librairie `opencv-python` pour capturer une image depuis la webcam.
- Comprendre la séparation des composants graphiques et de la logique de l'application.

## Librairies
- `pip install customtkinter`
- `pip install opencv-python`
- `pip install pillow`

## Composition de l'interface
### Fenêtre principale
- Un titre.
- Une zone pour afficher les différentes pages (layout).
- Deux bouton pour changer de layout (configuration zones / prise d'image).

### Layout Configuration zone
- Un bouton pour prendre une image.
- L'affichage de l'image prise.
- Un carré sur l'image pour définir la zone de capture.
- 4 zones de texte pour définir la position et la taille de la zone de capture.
- Un compteur qui affiche le nombre d'image prise pour la configuration.

### Layout Prise d'image
- Un bouton pour prendre une image (l'image et rognée à la zone de capture).
- L'affichage de l'image prise.
- Un compteur qui affiche le nombre d'image prise pour ce layout.

## Aide
### Prise d'image
Pour capturer une image depuis la webcam, nous allons utiliser la librairie `opencv-python`.

Pour capturer une image, nous allons utiliser la fonction `cv2.VideoCapture(0)`.
La valeur `0` correspond à l'indice de la webcam. Si vous avez plusieurs webcam, 
vous pouvez changer la valeur pour utiliser une autre webcam.

Pour afficher une image dans CustomTkinter, il faut utiliser le widget `Label`.

Pour capturer et afficher une image, vous pouvez vous inspirer du code suivant:

```python
import cv2
# Initialisation de la webcam
camera = cv2.VideoCapture(camera_index)

# Capture de l'image
ret, image = camera.read()
if not ret:
    raise RuntimeError("Échec lors de la capture de l'image")

# Affichage de l'image
label = ctk.CTkLabel(root)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
photo = ctk.CTkImage(Image.fromarray(image_rgb), size=(width, height))
label.configure(image=photo, text="")

# Libération de la webcam
camera.release()
```
