import os
from flask import Flask,render_template,request,send_from_directory
import cloudpickle as cp
import numpy as np
from urllib.request import urlopen

app=Flask(__name__)
model=cp.load(urlopen('https://raw.githubusercontent.com/steve-cse/Loan-Eligibility-LR/master/logistic_model.pkl'))

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsof.icon')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    new_credit = request.form['credit_input']
    new_education = request.form['education_input']
    new_gender = request.form['gender_input']

    new_credit=float(new_credit)
    new_gender = 1 if new_gender == "Male" else 0 if new_gender == "Female" else new_gender
    new_education = 1 if new_education == "Not Graduate" else 0 if new_education == "Graduate" else new_education

    features=[]
    features+=[new_credit,new_education,new_gender]
    prediction = model.predict(np.array(features).reshape(1, -1))
    if prediction[0]==1:
        result="Eligible for Loan"
    else:
        result= "Not Eligible for Loan"
    return render_template('index.html', **locals())

if __name__=='__main__':
    app.run()