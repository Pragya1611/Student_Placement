from flask import Flask, request, render_template
from utils import StudentInfo
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    Age = int(data['Age'])
    Gender = data['Gender']
    Stream = data['Stream']
    Internships = int(data['Internships'])
    CGPA = float(data['CGPA'])
    Hostel = int(data['Hostel'])
    HistoryOfBacklogs = int(data['HistoryOfBacklogs'])

    Obj = StudentInfo(Age, Gender, Stream, Internships, CGPA, Hostel, HistoryOfBacklogs)
    prediction = Obj.predict_placement()

    if prediction == 1:
        result = 'Placed'
    else:
        result = 'Not Placed'

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
