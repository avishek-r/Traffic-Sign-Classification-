import streamlit as st
import cv2
from tensorflow.keras.models import load_model
import numpy as np
model = load_model("model.h5")
classes = { 
    0:'Speed limit (20km/h)',
    1:'Speed limit (30km/h)', 
    2:'Speed limit (50km/h)', 
    3:'Speed limit (60km/h)', 
    4:'Speed limit (70km/h)', 
    5:'Speed limit (80km/h)', 
    6:'End of speed limit (80km/h)', 
    7:'Speed limit (100km/h)', 
    8:'Speed limit (120km/h)', 
    9:'No passing', 
    10:'No passing veh over 3.5 tons', 
    11:'Right-of-way at intersection', 
    12:'Priority road', 
    13:'Yield', 
    14:'Stop', 
    15:'No vehicles', 
    16:'Veh > 3.5 tons prohibited', 
    17:'No entry', 
    18:'General caution', 
    19:'Dangerous curve left', 
    20:'Dangerous curve right', 
    21:'Double curve', 
    22:'Bumpy road', 
    23:'Slippery road', 
    24:'Road narrows on the right', 
    25:'Road work', 
    26:'Traffic signals', 
    27:'Pedestrians', 
    28:'Children crossing', 
    29:'Bicycles crossing', 
    30:'Beware of ice/snow',
    31:'Wild animals crossing', 
    32:'End speed + passing limits', 
    33:'Turn right ahead', 
    34:'Turn left ahead', 
    35:'Ahead only', 
    36:'Go straight or right', 
    37:'Go straight or left', 
    38:'Keep right', 
    39:'Keep left', 
    40:'Roundabout mandatory', 
    41:'End of no passing', 
    42:'End no passing veh > 3.5 tons'
          } 
st.title("Traffic Sign Classification")
st.text("Detection of 42 traffic sign with ease")
st.markdown("Upload an image of the traffic sign")
img=st.file_uploader("")
submit = st.button('Predict')
st.sidebar.title('Developers Contact')
st.sidebar.markdown('[![Avishek Rijal]'
                        '(https://img.shields.io/badge/Author-Avishek--Rijal-lightgrey)]'
                        '(https://www.linkedin.com/in/avishek-rijal-0430801b1/)')
                        
if submit:


    if img is not None:

        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(img.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)



        # Displaying the image
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)
        #Resizing the image
        opencv_image = cv2.resize(opencv_image, (32,32))
        #Convert image to 4 Dimension
        opencv_image.shape = (1,32,32,3)
        #Make Prediction
        Y_pred = model.predict(opencv_image)
        ind = np.argmax(Y_pred)
        result = classes[ind]

        st.title(str("The model predicts the sign is "+result ))
 
