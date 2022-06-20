from flask import Flask, jsonify, request
import dental_scraper
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
scraper = dental_scraper


@app.route('/aia', methods=['POST'])
def AIAData():
    name = request.form['name']
    birth = request.form['birth']
    gender = request.form['gender']
    return jsonify(scraper.getAIAData(name, birth, gender))


@app.route('/lina', methods=['POST'])
def LinaData():
    name = request.form['name']
    birth = request.form['birth']
    gender = request.form['gender']
    return jsonify(scraper.getLinaData(name, birth, gender))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 