from flask import Flask, redirect, flash

def generate_key():
    import uuid
    
    return str(uuid.uuid4())

app = Flask(__name__)
app.secret_key = generate_key()

@app.route("/")
def re_direct():
    # flash("You are being redirected to the updated version of the site...")
    return redirect("https://sergeyyurkov1.herokuapp.com/adsb_tracker")

# app.run(port=8080)