#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/Jayraj/Prototype MK4/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

#pred_tomato_dieas = pred_sugarapple_dieas
#tomato_plant = sugar_apple

def pred_sugarapple_dieas(sugar_apple):
  test_image = load_img(sugar_apple, target_size = (256, 256)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)


  
  if pred==0:
      return "Canker_fruits-disease", 'Canker_fruits-disease.html'
       
  elif pred==1:
      return "Caterpillar worms leaf Disease", 'Caterpillar worms leaf Disease.html'
        
  elif pred==2:
      return "Faint color fruit disease", 'Faint color fruit disease.html'
        
  elif pred==3:
      return "InitialBurn leaf Disease", 'InitialBurn leaf Disease.html'
       
  elif pred==4:
      return "Myrtle Rust leaf disease", 'Myrtle Rust leaf disease.html'
        
  elif pred==5:
      return "Nutrition deficiency leaf disease", 'Nutrition deficiency leaf disease.html'
        
  elif pred==6:
      return "SemiBurn leaaf disease", 'SemiBurn leaaf disease.html'
        
  elif pred==7:
      return "crack_fruits_disease", 'crack_fruits_disease.html'
  elif pred==8:
      return "diplodia_fruits_disease", 'diplodia_fruits_disease.html'
        
  elif pred==9:
      return "fungi_fruits_disease", 'fungi_fruits_disease.html'
  elif pred==10:
      return "shrink leaf disease", 'shrink leaf disease.html'
  elif pred==11:
      return "uneven size fruit disease", 'uneven size fruit disease.html'

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('C:/Users/Jayraj/Prototype MK4/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_sugarapple_dieas(sugar_apple=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    
