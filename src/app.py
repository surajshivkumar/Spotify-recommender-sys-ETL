from flask import Flask, request, jsonify, render_template, send_from_directory

from flask_cors import CORS


app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    songs = ['blank space', 'stay']
    return render_template("search.html", songs=songs)

# @app.route("/recommend")
# def dashboard():
#     return render_template("dashboard.html")

@app.route("/results",methods=['POST'])
def results():
    '''
    Endpoint that handles the search functionality and displays results.
    '''
    if request.method == 'POST':
        searchTerm = request.form.get('search-term')
        #db search logic below
        results = ['test']
        return render_template('dashboard.html', results=results)



if __name__ == "__main__":
    app.run(debug=True, port=5002,threaded=False)