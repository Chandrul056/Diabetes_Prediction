from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi"

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            Pregnancies = int(request.form['pregnancies'])
            Glucose = int(request.form['glucose'])
            Bloodpressure = int(request.form['bloodpressure'])
            Skinthickness = int(request.form['skinthickness'])
            Insulin = int(request.form['insulin'])
            Bodymassindex = float(request.form['bodymassindex'])
            Diabetespedigreefunction = float(request.form['diabetespedigreefunction'])
            Age = int(request.form['age'])
        except ValueError:
            return jsonify("Please enter arguments")

        response =  jsonify(util.get_estimated_price(Pregnancies, Glucose, Bloodpressure, Skinthickness, Insulin, Bodymassindex, Diabetespedigreefunction, Age).tolist())

        response.headers.add('Access-Control-Allow-Origin','*')

        return response




if __name__ == "__main__":
    print("Starting Python Flask Server For Diabetes Prediction")
    util.load_saved_artifacts()
    app.run()
