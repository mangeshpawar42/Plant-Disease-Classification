import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/Jayraj/Prototype MK4/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

sugar_apple = cv2.imread('C:/Users/Jayraj/Prototype MK4/Dataset/test/IMG_20221029_173530.JPG')
test_image = cv2.resize(sugar_apple, (256,256)) # load image 
  
test_image = img_to_array(test_image)/255 # convert image to np array and normalize
test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
result = model.predict(test_image) # predict diseased palnt or not
  
pred = np.argmax(result, axis=1)
print(pred)


if pred==0:
    print( "Canker_fruits-disease")
       
elif pred==1:
    print("Caterpillar worms leaf Disease")
        
elif pred==2:
    print("Faint color fruit disease")
        
elif pred==3:
    print("InitialBurn leaf Disease")
       
elif pred==4:
    print("Myrtle Rust leaf disease")
        
elif pred==5:
    print("Nutrition deficiency leaf disease")
        
elif pred==6:
    print("SemiBurn leaaf disease")
        
elif pred==7:
      print("crack_fruits_disease")
      
elif pred==8:
      print("diplodia_fruits_disease")
        
elif pred==9:
      print("fungi_fruits_disease")
      
elif pred==10:
      print("shrink leaf disease")
      
elif pred==11:
      print("uneven size fruit disease")
