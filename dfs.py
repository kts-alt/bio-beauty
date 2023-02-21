try:
    from deepface import DeepFace
except Exception as e:
    print("first init failed")

from deepface import DeepFace
print("init...")    

import cv2
import matplotlib.pyplot as plt

img_path = "static/images/saved_img.jpg"
# if img_path has a value, create a function that runs the deepface function. If no value
actions = ['age', 'gender', 'race', 'emotion']

img = cv2.imread(img_path)

plt.imshow(img)

objs = DeepFace.analyze(img_path, actions)