from flask import Flask, request, jsonify, render_template
from cover_letter import cover_letter_generator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/coverletter',methods=["POST"])
def cover_letter():
    body = request.get_json()
    res = cover_letter_generator(url=body.get('url'), company=body.get('company'))
    return jsonify(res)


if __name__ == "__main__":
    app.run()