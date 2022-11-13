from flask import Flask
import numpy as np
import pandas as pd
import os
import tensorflow as tf
import requests
from flask import Flask, request, render_template
from keras.preprocessing import image
from keras.models import load_model
import pickle


model= pickle.load(open('dt_model.pkl', 'rb'))

my_app =Flask(__name__)

@my_app.route('/')
def home():
    return render_template('index.html')

@my_app.route("/index.html")
def index():
    return render_template("index.html")


@my_app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']  # fetch input
        filename = file.filename

@my_app.route('/crop_prediction', methods=['POST'])
def crop_prediction():
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potassium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = model.predict(data)
        final_prediction = my_prediction[0]
        return render_template('crop_result.html', prediction=final_prediction, pred='img/crop/'+final_prediction+'.jpg')

if __name__ == "__main__":
    my_app.run()