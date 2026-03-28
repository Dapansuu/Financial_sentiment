import tensorflow as tf
import os

model = tf.keras.models.load_model('models/sentiment.keras')
version = os.listdir("serving_model/sentiment")
print(version)

max_version = max([int(i) for i in version]) if version else 0
version = max_version + 1
print(f"Exporting model version: {version}")
export_dir = f"serving_model/sentiment/{version}"
model.export(export_dir)
