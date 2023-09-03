from flask import Flask, request, jsonify, render_template
from backend import rag

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat')
def chat():
    query = request.args.get("input")
    res = rag(query)
    return jsonify(res)


if __name__ == "__main__":
    app.run()