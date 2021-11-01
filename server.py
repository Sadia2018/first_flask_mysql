from flask.templating import render_template
from flask import Flask, render_template, request, redirect
from friend import Friend
app = Flask(__name__)
@app.route('/')
def index(): 
    
    return render_template("index.html")
@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    
    

    
    
    
