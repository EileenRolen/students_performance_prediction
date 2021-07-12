# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model
filename = 'ridge_regression.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        absences = int(request.form['absences'])
        G1 = int(request.form['G1'])
        G2 = int(request.form['G2'])
        
        studytime = request.form['studytime']
        if studytime == '2':
            temp_array = temp_array + [1,0,0,0]
        elif studytime == '3':
            temp_array = temp_array + [0,1,0,0]
        elif studytime == '1':
            temp_array = temp_array + [0,0,1,0]
        elif studytime == '4':
            temp_array = temp_array + [0,0,0,1]
            
        
                     
        
       
        
            
        failures = request.form['failures']
        if failures == '0':
            temp_array = temp_array + [1,0,0,0]
        elif failures == '3':
            temp_array = temp_array + [0,1,0,0]
        elif failures == '1':
            temp_array = temp_array + [0,0,1,0]
        elif failures == '2':
            temp_array = temp_array + [0,0,0,1]
        
           
       
        higher = request.form['higher']
        if higher == 'yes':
            temp_array = temp_array + [1,0]
        elif higher == 'no':
            temp_array = temp_array + [0,1]
      
        
      
        temp_array = temp_array + [absences,G1,G2]
        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
            
        return render_template('result.html', lower_limit = my_prediction-1, upper_limit = my_prediction+2)


if __name__ == '__main__':
	app.run(debug=True)