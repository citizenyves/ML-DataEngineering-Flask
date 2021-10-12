from flask import Flask, render_template, redirect, request, url_for
import numpy as np
import random
import joblib

app = Flask(__name__)

# 메인 페이지
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# 예측 값 출력 페이지
@app.route('/predict', methods=['POST', 'GET'])
def make_prediction():
    while request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])
        num4 = int(request.form['num4'])
        num5 = int(request.form['num5'])
        num6 = int(request.form['num6'])

        if (0 < num1 <= 45 and 0 < num2 <= 45 and 0 < num3 <= 45 and 0 < num4 <= 45 and 0 < num5 <= 45 and 0 < num6 <= 45):
            # 2d array
            data = [[num1, num2, num3, num4, num5, num6]]
            # data_2d = np.reshape(data, (-1, 1))

            # to predict
            model = joblib.load('/Users/mac/project-sec3/flask_app/model/model.pkl')
            predict = str(model.predict(data)[0])

            # returning of predict must be str, dict, ... not a ndarray, a list.
            return render_template('prediction.html', predict=predict)
    
        else:
            return "YOU PUT SOME WRONG NUMS MAN"


# Flask error handling decorator
@app.errorhandler(404)
def page_not_found(error):
    return "NO PAGE, CHECK YOUR URL", 404


if __name__ == '__main__':
    app.run(debug=True)