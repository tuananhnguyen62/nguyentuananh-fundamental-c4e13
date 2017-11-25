from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the program of BMI assessment"

@app.route('/bmi/<float:w>/<float:h>')
def bmi(w, h):
    bmi = w / (h*h)
    if bmi < 16:
        return "Your BMI is: {}. You are Severely underweight".format(str(bmi))
    elif bmi < 18.5:
        return "Your BMI is: {}. You are Underweight".format(str(bmi))
    elif bmi < 25:
        return "Your BMI is: {}. You are Normal".format(str(bmi))
    elif bmi < 30:
        return "Your BMI is: {}. You are Overweight".format(str(bmi))
    else:
        return "Your BMI is: {}. You are Obese".format(str(bmi))


if __name__ == '__main__':
  app.run(debug=True)
