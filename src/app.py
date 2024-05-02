from flask import Flask, request, jsonify, render_template, send_from_directory

from flask_cors import CORS


app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/recommend")
def dashboard():
    return render_template("dashboard.html")




if __name__ == "__main__":
    app.run(debug=True, port=5002,threaded=False)