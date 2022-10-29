# Plant-Disease-Detection
Detecting diseases in staple food plants for early diagnosis like potatoes, tomatoes etc.

# The CNN model
Used the model designed in Plant-Disease-Detetion/main.py to learn and predict two most widespread and common diseases in potato plants namely, Early and Late blight.
Consists of a data augmentation and resize layer and the whole model is saved in two forms in the folder Plant-Disease-Detetion/actual_model. One is the tensor model and the other one as a keras model(.h5).

# Google Cloud Deployment
The model was deployed to google cloud to be called as a function(predict) from anywhere around the world which would send the results back to the clients machine.The function is present in Plant-Disease-Detection/gcp/main.py and was deployed using Google Cloud SDK Shell.

# Two ways of deployment of model
## The model has been deployed as a mobile app as well as a webapp.
### 1. The Mobile app 
### 2. The Webapp
       The webapp is built on top of FAST-Api services for hosting. This Api is present in Plant-Disease-Detetion/api/main2.py
