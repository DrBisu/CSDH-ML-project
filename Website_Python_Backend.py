import pandas as pd
from tensorflow import keras
import tensorflow as tf
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")
import lime
import dill
import matplotlib.pyplot as plt

#Clone the github repository and unzip the final_model.zip

#The trained model is the final_model1 sub-folder that is inside the content folder of the unzipped file

#Load the model from the repository

model = keras.models.load_model('*insert file path to the "final_model1" sub-folder*')

#Load the scaler from the repository

scaler = pickle.load(open('*insert file path to the "scaler.sav" folder*', 'rb'))

#Load the LIME explainer from the repository

with open('*insert file path to the "LIME_explainer" file in the cloned repository*', 'rb') as f:     
  explainer = dill.load(f)

#Define the function that performs the prediction

def model_prediction (model, scaler, age, headache, dementia, motor, midline, size, qol):
    
    #Store the input parameters
    userinput_age = age
    userinput_headache = headache
    userinput_dementia = dementia
    userinput_motor = motor
    userinput_midline = midline
    userinput_size = size
    userinput_qol = qol
    
    #Normalize the "Age" input parameter
    userinput_age = np.reshape(userinput_age, (1,-1))
    test_scaled_set = scaler.transform(userinput_age)
    
    #Creat the final input array
    test = [test_scaled_set, userinput_headache, userinput_dementia, userinput_motor, userinput_midline, userinput_size, userinput_qol]
    finalArray = np.asarray(test, dtype = np.float64, 
                        order ='C')

    henry = np.transpose(finalArray)
    test= pd.DataFrame(data = henry, index=['age','headache' ,'dementia','Motor weakness', 'midline shift', 'CSDH size','Pre-morbid QoL']) 
    test = test.T
    
    #Predict the output
    
    prediction = model.predict(test)
    
    return prediction, test


#Call the function to generate the output

#age, dementia, headache, dementia, motor, midline, size, qol are the input parameters defined by the user

final_prediction, test = model_prediction(model, scaler, age, headache, dementia, motor, midline, size, qol)

#Print probability of the output

final_prediction = final_prediction.flatten()
final_prediction = final_prediction*100
final_prediction = '%.3f' % final_prediction
print(f"P (Acceptance) = {str(final_prediction).replace('[', '').replace(']', '')}%") #Output 1

#Print prediction

if final_prediction > 0.5:
    print("Accepted")  #Output 2
else:
    print("Rejected")  #Output 2
  
#Generate the LIME explanation

finalArray = test.flatten()
finalArray = np.transpose(finalArray)

explain = explainer.explain_instance(finalArray, model.predict,top_labels=1)
with plt.style.context("ggplot"):
  lime_output = explain.as_pyplot_figure(label = 0) #Output 3

