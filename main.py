from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template('homepage.html')

@app.route('/predict', methods=['POST'])
def predict():
	height = float(request.form.get("height"))
	weight = float(request.form.get('weight'))
	bp = float(request.form.get('bp'))
	glucose = float(request.form.get('glucose'))
	insulin = float(request.form.get('insulin'))
	age = float(request.form.get('age'))

	bmi = weight/height**2
	feature_array = [glucose, bp, insulin, bmi, age]
	
	model = pickle.load(open('model.pkl','rb'))
	prediction = model.predict([feature_array])
	return render_template('result.html', prediction=prediction, bmi=bmi)

"""
@app.route('/result',methods=['POST','GET'])
def result():
	if request.method == 'POST':
		result = request.form
		return render_template('result.html', result=result)
"""
if __name__ == "__main__":
    app.run(debug=True)
