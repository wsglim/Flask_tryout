from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def home():
    return "<p>Hallo wereld! Dit is het huiswerk van hoofdstuk 10.</p>"


if __name__=='__main__':
    app.run(port=5000,debug=True)

