from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
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
		if prediction == 0 :
			ans = 'No diabetes'
		else:
			ans = 'Diabetes'
		return render_template('homepage.html', answer=ans, bmi=bmi)

	return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)
