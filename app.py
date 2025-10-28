from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/decorate', methods=['GET'])
def decorate():
    return jsonify({"message": "API funcionando!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
