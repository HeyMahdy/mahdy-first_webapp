from flask import Flask, render_template , jsonify

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
  ,
  {
    'id' : 4,
    'title' : 'Event Organizer',
  
  }
]
@app.route('/')
def Hello_world():
    return render_template('home.html',jobs=JOBS)
@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)
print(__name__)
if (__name__== "__main__") :
    app.run(host='0.0.0.0', debug=True)
  