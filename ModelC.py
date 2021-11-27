import numpy as np
import pandas as pd
import PIL.ImageOps
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
from flask import Flask,jsonify,request
from classifier import get_prediction


X = np.load('image_npz')['arr_0']
Y = pd.read_csv("labels.csv")["labels"]
print(pd.Series(Y).value_count())
classes = ["A",'"B',"C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nclasses = len(classes)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state = 9,train_size = 3500, test_size = 500)


def get_prediction(image):
    im_pil = Image.open(image)
    image_bw = im_pil.convert('L')
    image_bw_resized = image_bw.resize((28,28),Image.ANTIALIAS)
    pixel_filter = 20
    min_pixel = np.precentile(image_bw_resized, pixel_filter)
    image_bw_resized_inverted_scaled = np.clip(image_bw_resized-min_pixel,0,255)
    max_pixel = np.max(image_bw_resized)
    image_bw_resized_inverted_scaled = np.asarray(image_bw_resized_inverted_scaled)/max_pixel
    test_sample = np.array(image_bw_resized_inverted_scaled).reshape(1,660)
    test_pred = clf.predict(test_sample)
    return test_pred[0]

app = Flask(__name__)
def predict_data():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)
    return jsonify({
        "prediction": prediction
    }),200

if(__name__=='__main__'):
    app.run(debug = True)