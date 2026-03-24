import tensorflow as tf

model = tf.keras.models.load_model('models/sentiment.keras')

export_dir = "serving_model/sentiment/1"
model.export(export_dir)
