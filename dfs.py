try:
    from deepface import DeepFace
except Exception as e:
    print("first init failed")

from deepface import DeepFace
print("initialized")    

img_path = "static/images/saved_img.jpg"
actions = ['age', 'gender', 'race', 'emotion']

objs = DeepFace.analyze(img_path, actions, enforce_detection=False)

if objs[0]['dominant_gender'] == 'Man':
    print("We've got a guy over here!")
else:
    print("We've guy a girl over here!")