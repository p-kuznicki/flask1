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
    playlist = []
    playlist.append(url_for('static', filename='cmok.mp3'))
    playlist.append(url_for('static', filename='1.mp3'))
    if session['assassin']:
        playlist.append(url_for('static', filename='2.mp3'))
    if session['mordred']:
        playlist.append(url_for('static', filename='3.mp3'))
    if session['morgana']:
        playlist.append(url_for('static', filename='4.mp3'))
    playlist.append(url_for('static', filename='5.mp3'))
    if session['lancelot']:
        playlist.append(url_for('static', filename='6.mp3'))
    playlist.append(url_for('static', filename='pause.mp3'))
    playlist.append(url_for('static', filename='cmok.mp3'))
    playlist.append(url_for('static', filename='7.mp3'))
    if session['mordred']:
        playlist.append(url_for('static', filename='8.mp3'))
    if session['oberon']: 
        playlist.append(url_for('static', filename='9.mp3'))
    if session['merlin']:  
        playlist.append(url_for('static', filename='10.mp3'))
        playlist.append(url_for('static', filename='pause.mp3'))
        playlist.append(url_for('static', filename='cmok.mp3'))
        playlist.append(url_for('static', filename='11.mp3'))
    if session['parsifal']: 
        playlist.append(url_for('static', filename='12.mp3'))
    if session['morgana']:
        playlist.append(url_for('static', filename='13.mp3'))
    if session['parsifal']: 
        playlist.append(url_for('static', filename='14.mp3'))
        playlist.append(url_for('static', filename='pause.mp3'))
        playlist.append(url_for('static', filename='cmok.mp3'))
        playlist.append(url_for('static', filename='15.mp3'))
    playlist.append(url_for('static', filename='16.mp3'))
    playlist.append(url_for('static', filename='cmok.mp3'))
    return render_template('night.html', playlist = playlist)

if __name__ == '__main__':
    app.run(debug=True)


