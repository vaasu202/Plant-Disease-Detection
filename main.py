import tensorflow as tf
from keras import models, layers


channel_size = 3
Epochs = 50
Batch_size = 32
img_size = 256

#Loading the dataset from the directory
dataset = tf.keras.utils.image_dataset_from_directory(
    directory="PlantVillage",
    labels='inferred',
    label_mode='int',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(256, 256),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False,
)
#Batch size 32 with 2152 samples. Therfore, 68 divisions
train_dd = dataset.take(54)
test_dd = dataset.skip(54)
val_ds = test_dd.take(6)
test_dd = test_dd.skip(6)

#For confirmed size dimensions
resize_rescale = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.Resizing(256,256),
    tf.keras.layers.experimental.preprocessing.Rescaling(1.0/255)
])

#Data Augmentation for more training samples
data_aug = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
    tf.keras.layers.experimental.preprocessing.RandomRotation(0.2)
])
n_class = 3
input_shape1 = (Batch_size,img_size,img_size,channel_size)
model = models.Sequential([
    resize_rescale,
    data_aug,
    layers.convolutional.Conv2D(32,(3,3),activation="relu",input_shape=(256,256)),
    layers.MaxPooling2D((2,2)),
    layers.convolutional.Conv2D(64,kernel_size=(3,3),activation="relu"),
    layers.MaxPooling2D((2,2)),
    layers.convolutional.Conv2D(64,kernel_size=(3,3),activation="relu"),
    layers.MaxPooling2D((2,2)),
    layers.convolutional.Conv2D(64,(3,3),activation="relu"),
    layers.MaxPooling2D((2,2)),
    layers.convolutional.Conv2D(64,(3,3),activation="relu"),
    layers.MaxPooling2D((2,2)),
    layers.convolutional.Conv2D(64,(3,3),activation="relu"),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64,activation="relu"),
    #to normalise probablility of classes
    layers.Dense(n_class,activation="softmax")

])

#Building the model
model.build(input_shape=input_shape1)
#model.summary()

#Compiling the model
model.compile(
    optimizer="adam",
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics = ["accuracy"]
)
red = model.fit(
    train_dd,
    epochs=Epochs,
    batch_size=Batch_size,
    verbose=1,
    validation_data=val_ds,
)

score = model.evaluate(test_dd)
model.save("/actual_mod/mymodel_for_mobile.h5")




