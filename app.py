from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return 'Hello thatpong!'

@app.route('/Id')
def Id():
    return '654272106'

@app.route('/name')
def name():
    return 'thatpong koommueng'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

if _name_ == '_main_':
    app.run(debug=True)