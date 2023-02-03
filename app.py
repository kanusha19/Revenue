from flask import Flask
app = Flask(__name__)

@app.route("/status")
def status():
    return "Hello from Rasa"

if __name__ == '__main__':
    app.run(port=5005)
