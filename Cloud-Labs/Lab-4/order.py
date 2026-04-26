from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/order")
def order():
    try:
        res = requests.get("http://product-service:5001/product")
        return jsonify({"order": "success", "product": res.json()})
    except:
        return jsonify({"order": "failed", "reason": "product service down"})

app.run(host="0.0.0.0", port=5002)