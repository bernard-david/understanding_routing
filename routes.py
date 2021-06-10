from flask import Flask
app = Flask(__name__)
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')          
def dojo():
    return 'Dojo!'
@app.route('/say/<string:name>')
def say(name):
    print(name)
    return "Hi, " + name
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    print(num)
    print(word)
    return num * word
@app.route('/<path:path>')
def cath_all(path):
    return "Sorry! No response. Try again."
if __name__=="__main__":
    app.run(debug=True) 