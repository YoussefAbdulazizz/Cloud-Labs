from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/product")
def product():
    return jsonify({"product": "Laptop", "price": 1000})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)