from flask import Flask, render_template, redirect, url_for, session
from forms import AvalonForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'baldursgate'

@app.route('/', methods=['GET', 'POST'])
def choice():
    form = AvalonForm()
    if form.validate_on_submit():
        session['merlin'] = form.merlin.data
        session['assassin'] = form.assassin.data
        session['parsifal'] = form.parsifal.data
        session['lancelot'] = form.lancelot.data
        session['morgana'] = form.morgana.data
        session['mordred'] = form.mordred.data
        session['oberon'] = form.oberon.data
        return redirect(url_for('night'))
    return render_template('choice.html', form=form)

@app.route('/night')
def night():
    return render_template('night.html')

if __name__ == '__main__':
    app.run(debug=True)


