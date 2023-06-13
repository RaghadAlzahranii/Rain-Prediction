from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def main():
    return render_template("rain.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('rain.html',pred='There is a chance of rain today!.\n Probability of rain is {}'.format(output))
    else:
        return render_template('rain.html',pred='There is no chance of rain today!.\n Probability of rain is {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True, port=5001)