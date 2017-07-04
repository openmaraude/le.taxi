from flask import Flask, redirect

app = Flask(__name__)
@app.route('/stats'):
    return redirect('https://api.taxi/stats', code=302)
