from flask import Flask, request, render_template

app = Flask(__name__)

#@app.route('/')
#def welcome():
#    return 'This is my homepage'

@app.route('/blog')
def blog():
    return 'This is my blog page'

@app.route('/', methods=['GET', 'POST'])
def payment():

    name = ''
    city= ''
    weight = 0
    height = 0
    result = 0

    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        city = request.form.get('usercity')
        weight = request.form.get('weight')
        height = request.form.get('height')
        result = round(float(weight)/((float(height)/100)**2))

    return render_template('index.html', name=name, city=city, weight=weight, height=height, result=result)



#To run the Flask App
app.run()
