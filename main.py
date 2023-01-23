import pickle as pkl
import numpy as np
model = pkl.load(open('logistic_model.pkl', 'rb')) # rb means read as binary
Credit_History = 1
Education = 0
Gender = 0
lst=[]
lst+=[Credit_History,Education,Gender]
result = model.predict(np.array(lst).reshape(1, -1))
print (result)