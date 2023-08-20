from flask import Flask, request, jsonify, render_template
from backend import domain_name_generator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat')
def chat():
    niche = request.args.get("input")
    res = domain_name_generator(niche)
    return jsonify(res)


if __name__ == "__main__":
    app.run()