from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is Tuan Anh's site for Homework"

@app.route('/about-me')
def about_me():
    return render_template('index1.html')

@app.route('/school')
def hello():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
