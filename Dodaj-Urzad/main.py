from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



# Tworzenie obiektow
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urzedy.db'
db = SQLAlchemy()
db.init_app(app)



# Tworzenie struktury bazy danych
class Urzad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Miasto = db.Column(db.String(250), nullable=False)
    urzad = db.Column(db.String(250), nullable=False)
    adres = db.Column(db.String(250), nullable=False)
    telefon = db.Column(db.Integer(), nullable=False)
    faks = db.Column(db.Integer(), nullable=False)
    strona = db.Column(db.String(250), nullable=False)
    BIP = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    godziny = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


# Strona glowna
@app.route('/')
def home():
    return render_template('index.html')


# Strona do dodania nowego urzedu do bazy danych
@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    if request.method == 'POST':
        with app.app_context():
            # tworzenie nowego rekordu w bazie danych
            nowy_urzad = Urzad(
                Miasto=request.form['miasto'],
                urzad=request.form['miejscowosc'],
                adres=request.form['adres'],
                telefon=request.form['telefon'],
                faks=request.form['faks'],
                strona=request.form['strona'],
                BIP=request.form['bip'],
                email=request.form['email'],
                godziny=request.form['pon'])
            db.session.add(nowy_urzad)
            db.session.commit()

    return render_template('dodaj.html')


# Strona do usuniencia urzedu z bazy dancyh
@app.route('/usun', methods=['GET', 'POST'])
def usun():
    if request.method == 'POST':
        miasto = request.form['Miasto']
        urzad = db.session.query(Urzad).filter_by(Miasto=miasto).first()
        db.session.delete(urzad)
        db.session.commit()

    return render_template('usun.html')


# Strona do pokazania wybranego przez uzytkownika danych danego urzedu
@app.route('/pokaz', methods=['GET', 'POST'])
def pokaz():
    if request.method == 'POST':
        miasto = request.form['Miasto']
        urzad = db.session.query(Urzad).filter_by(Miasto=miasto).first()
        return render_template('pokaz.html', miasto=urzad)

    return render_template('pokaz.html')


# Startuje alikacje
if __name__ == '__main__':
    app.run(debug=True)

