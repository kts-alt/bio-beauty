try:
    from deepface import DeepFace
except Exception as e:
    print("first init failed")

from deepface import DeepFace
print("initialized")    

img_path = "static/images/saved_img.jpg"
actions = ['age', 'gender', 'race', 'emotion']

objs = DeepFace.analyze(img_path, actions, enforce_detection=False)