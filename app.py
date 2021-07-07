# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model
filename = 'student_perfo_modl.pkl'
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
            
        Medu = request.form['Medu']
        if Medu == '4':
            temp_array = temp_array + [1,0,0,0,0]
        elif Medu == '1':
            temp_array = temp_array + [0,1,0,0,0]
        elif Medu == '3':
            temp_array = temp_array + [0,0,1,0,0]
        elif Medu == '2':
            temp_array = temp_array + [0,0,0,1,0]
        elif Medu == '0':
            temp_array = temp_array + [0,0,0,0,1]
            
        Fedu = request.form['Fedu']
        if Fedu == '4':
            temp_array = temp_array + [1,0,0,0,0]
        elif Fedu == '1':
            temp_array = temp_array + [0,1,0,0,0]
        elif Fedu == '2':
            temp_array = temp_array + [0,0,1,0,0]
        elif Fedu == '3':
            temp_array = temp_array + [0,0,0,1,0]
        elif Fedu == '0':
            temp_array = temp_array + [0,0,0,0,1]
                     
        
             
        Mjob = request.form['Mjob']
        if Mjob == 'teacher':
            temp_array = temp_array + [1,0,0,0,0]
        elif Mjob == 'other':
            temp_array = temp_array + [0,1,0,0,0]
        elif Mjob == 'services':
            temp_array = temp_array + [0,0,1,0,0]
        elif Mjob == 'health':
            temp_array = temp_array + [0,0,0,1,0]
        elif Mjob == 'at_home':
            temp_array = temp_array + [0,0,0,0,1]
            
        Fjob = request.form['Fjob']
        if Fjob == 'at_home':
            temp_array = temp_array + [1,0,0,0,0]
        elif Fjob == 'health':
            temp_array = temp_array + [0,1,0,0,0]
        elif Fjob == 'other':
            temp_array = temp_array + [0,0,1,0,0]
        elif Fjob == 'services':
            temp_array = temp_array + [0,0,0,1,0]
        elif Fjob == 'teacher':
            temp_array = temp_array + [0,0,0,0,1]
      
            
        health = request.form['health']
        if health == '1':
            temp_array = temp_array + [1,0,0,0,0]
        elif health == '2':
            temp_array = temp_array + [0,1,0,0,0]
        elif health == '3':
            temp_array = temp_array + [0,0,1,0,0]
        elif health == '4':
            temp_array = temp_array + [0,0,0,1,0]
        elif health == '5':
            temp_array = temp_array + [0,0,0,0,1]
           
        paid = request.form['paid']
        if paid == 'no':
            temp_array = temp_array + [1,0]
        elif paid == 'yes':
            temp_array = temp_array + [0,1]
            
        higher = request.form['higher']
        if higher == 'no':
            temp_array = temp_array + [1,0]
        elif higher == 'yes':
            temp_array = temp_array + [0,1]
            
        internet = request.form['internet']
        if internet == 'no':
            temp_array = temp_array + [1,0]
        elif internet == 'yes':
            temp_array = temp_array + [0,1]
        
        
        temp_array = temp_array + [absences,G1,G2]
        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', lower_limit = my_prediction-1, upper_limit = my_prediction+1)


if __name__ == '__main__':
	app.run(debug=True)