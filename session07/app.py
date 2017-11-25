from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def index():
    return "Hello C4E13"
#
# @app.route('/hello/tuananh')
# def hello_me():
#     return "Hello Anh"
#
# @app.route('/<lastname>/<firstname>')
# def hello(lastname, firstname):
#     return "Hello " + lastname + " " + firstname
#
# @app.route('/sum/<int:a>/<int:b>')
# def sum(a, b):
#     sumab= a + b
#     return "Sum cua 2 so la: " + str(sumab)

if __name__ == '__main__':
  app.run(debug=True)
