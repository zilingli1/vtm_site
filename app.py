from flask import Flask
from flask import render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='AboutVTM')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        Total=''
        TankRadius=float(form['radius'])
        TankHeight=float(form['height'])
        Total=(((3.14*TankRadius*TankRadius)+(2*(3.14*(TankRadius*TankHeight))))/144)*25 + (((3.14*TankRadius*TankRadius)+(2*(3.14*(TankRadius*TankHeight))))/144)*15
        return render_template('estimate.html', Total=Total, pageTitle='Tank Painting Estimate')
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)