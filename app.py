from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def choice():
    return render_template('choice.html')

if __name__ == '__main__':
    app.run(debug=True)
