from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
  {
     'id' : 1,
     'title' : 'Marketing',
     },
  {
     'id' : 2,
     'title' : 'human resources',
     },
  {
     'id' : 3,
     'title' : 'Admin',
     }
]
@app.route('/')
def Hello_world():
    return render_template('home.html')

print(__name__)
if (__name__== "__main__") :
    app.run(host='0.0.0.0', debug=True)
  