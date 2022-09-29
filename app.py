from flask import Flask, jsonify, request
from get_news import get_data

app = Flask(__name__)

@app.route("/")
def index():
    return "Server is running, go to /news"

@app.route('/news', methods=['GET'])
def get_news():
    return get_data()


if __name__ == '__main__':
    app.run(debug=True)
