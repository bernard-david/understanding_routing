from flask import Flask
app = Flask(__name__)
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')          
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi, " + str(name)
@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    print(num)
    print(word)
    return int(num) * str(word)
@app.route('/<path:path>')
def cath_all(path):
    return "Sorry! No response. Try again."
if __name__=="__main__":
    app.run(debug=True) 