from flask import Flask, request, render_template, redirect, url_for
import pickle


app = Flask(__name__)
g = pickle.load(open("gender_classifier.pkl", "rb"))


@app.route('/')
def home():
    return redirect(url_for('gender_classifier'))

@app.route('/gender_classifier', methods = ["GET", "POST"])
def gender_classifier():
    if request.method == "POST":
        height = request.form['height']
        weight = request.form['weight']
        
        height = float(height) / 2.54
        weight = float(weight) * 2.205
        
        gender = g.predict([[height, weight]])
        
        if gender[0] == 'Male':
            gender_svg = url_for('static', filename = "svg/male.svg")
        else:
            gender_svg = url_for('static', filename = "svg/female.svg")
        return render_template('index.html', gender = gender[0], gender_svg = gender_svg)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug = True)