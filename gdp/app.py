from flask import Flask, render_template, request
import requests
import flask
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

df = pd.read_csv("Admission_Predict_Ver1.1.csv")

df.drop('Serial No.', axis=1, inplace=True)

df.columns = ['GRE_Score', 'TOEFL_Score', 'University_Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance of Admit']

X = df.drop(labels='Chance of Admit', axis=1)

y = df['Chance of Admit']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.3)

LR = LinearRegression()

LR.fit(X_train, y_train)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        gre = request.form['GRE Score'].replace(" ", "")
        toefl = request.form['TOEFL Score'].replace(" ", "")
        rank = request.form['University Rating'].replace(" ", "")
        sop = request.form['SOP'].replace(" ", "")
        lor = request.form['LOR'].replace(" ", "")
        cgpa = request.form['CGPA'].replace(" ", "")
        research = request.form['Research'].replace(" ", "")

        gre, toefl, rank, sop, lor, cgpa, research = int(gre), int(toefl), float(rank), float(sop), float(lor), float(cgpa), int(research)

        result = LR.predict([[gre, toefl, rank, sop, lor, cgpa, research]])

        return render_template('results.html', result=result)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

