import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import io
import base64
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.image as mpimg


app = Flask(__name__)
model = pickle.load(open('model_cc', 'rb'))

ref_df = pd.read_pickle("ref_df.pkl")



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    in_d = [x for x in request.form.values()]
    size_tag = "full_size"
    test = [in_d[7], in_d[0], in_d[1], in_d[3], size_tag , in_d[5], in_d[6], in_d[2], in_d[4]]
    
    
    test[-2] = int(test[-2])
    test[-1] = float(test[-1])
    
    test_df = pd.DataFrame([test], columns = ['year','odometer', 'region_ind', 'manufacturer_ind', 'model_ind', 'condition_ind', 'size_ind', 'type_ind', 'state_ind'])
    list_test = []
    for i in range(0, 7):
        m = test[i]
        ind = ref_df["Index_val"][i]
        try:
            list_test.append(ind[m])
        except:
            list_test.append(10)

    test_ref_df = pd.DataFrame(columns = ['region_index', 'manufacturer_index', 'model_index', 'condition_index', 'size_index', 'type_index', 'state_index'])
    test_ref_df = test_ref_df.append({'region_index' : list_test[0], 'manufacturer_index': list_test[1], 'model_index': list_test[2], 'condition_index': list_test[3], 'size_index': list_test[4], 'type_index': list_test[5], 'state_index':list_test[6]},
               ignore_index = True)
    test_data = (test[7:9])+(test_ref_df.iloc[0].tolist())
    
    predicted_price = model.predict([test_data])[0]

    output = round(predicted_price, 2)

    return render_template('index.html', prediction_text='Predicted Price of your Car is:  $ {}'.format(output))

    
@app.route('/visual0')
def visual0():  
    
    wordcloud = mpimg.imread('wordcloud.png') 
    
    return Response(wordcloud.getvalue(), mimetype='image/png')



    
#if __name__ == "__main__":
 #   app.run(debug=True)