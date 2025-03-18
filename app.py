from flask import flash, Flask

app=Flask(__name__)
@app.route('/')
def index():
    return "Bienvenu sur mon site"
if __name__== "__main__":
    app.run(debug=True)


