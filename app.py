import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/weatherapp', methods = ['POST', 'GET'])
def getweatherdata():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {
        'q': request.form.get('city'),
        'appid': request.form.get('appid'),  
        'units': request.form.get('units')
    }
    response = requests.get(url, params=param)
    data = response.json()  

    return f"Current temperature in {data['name']} is {data['main']['temp']} degrees Fahrenheit."


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port= 5002)


