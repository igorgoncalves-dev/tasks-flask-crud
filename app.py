from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/about')
def about():
    return 'About this corp'

if __name__ == "__main__":
    app.run(debug=True)