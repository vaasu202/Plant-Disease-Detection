## Incase of a web app ##

import numpy as np
from fastapi import FastAPI, File,UploadFile
import uvicorn
from io import BytesIO
from PIL import Image
import tensorflow as tf


MODEL = tf.keras.models.load_model("../actual model/mymodel_for_mobile.h5")
CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]


app = FastAPI()
@app.get("/ping")
async def ping():
    return "You found me"

def read_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_image(await file.read())
    img_batch = np.expand_dims(image,0)
    print(img_batch)
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        "Class": predicted_class,
        "Confidence": float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app,port=8000,host="localhost")