## For mobile devices ##

from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np

BUCKET = "boom155" ##google cloud name
CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]

model = None

def download_blob(bucket_name,source_blob_name,destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET,
            "models/mymodel_for_mobile.h5",
            "/tmp/mymodel_for_mobile.h5",
        )
        model = tf.keras.models.load_model("/tmp/mymodel_for_mobile.h5")

    image = request.files["file"]
    image = np.array(Image.open(image).convert("RGB").resize((256,256)))
    img_array = tf.expand_dims(image,0)
    print(img_array)
    predictions = model.predict(img_array)
    print("Predictions:", predictions)
    index = np.argmax(predictions)
    print("index",index)
    predicted_class = CLASS_NAMES[index]
    confidence = round(100 * (np.max(predictions)), 2)

    return {"class": predicted_class, "confidence": confidence}