# save this as app.py
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # Variable wo ich sage, dass ich ein neue App erstellen will
                      #(befindet sich alle Information über mein aktuell Flask Project)

# Configuration für unsere SQL DatenBank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(200), nullable = True)
    content = db.Column(db.String(500), nullable = True)
    created_at = db.Column(db.DateTime(), default = datetime.utcnow)

@app.route("/<name>", methods= ['GET', 'POST']) # Se puede añadir despues del / depende de que pag quiera crear
def start_page(name):
    if request.method == 'POST':
        # Mit diesem Logic stehen ein neue Zeile in meine Datenbank
        new_message = Message( 
            user = name,
            content = request.form['content']
        )
        db.session.add(new_message)
        db.session.commit() # Speichern den Daten an 
    messages = Message.query.order_by(Message.created_at).all() # Alle nachrichten sind abgefragt
    return render_template('index.html', messages = messages, name = name) # Corre la app que yo quiero

if __name__ == "__main__":
    app.run(debug=True)
