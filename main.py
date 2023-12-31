from flask import Flask, render_template, request
import random
import sqlite3
from pathlib import Path

app = Flask(__name__)

db_path = Path("lottery_data.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS lottery_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gewinn REAL
    )
''')

conn.commit()
conn.close()

def add_to_lottery_data(gewinn):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lottery_data (gewinn) VALUES (?)", (gewinn,))
    conn.commit()
    conn.close()

def get_total_gewinn():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(gewinn) FROM lottery_data")
    total_gewinn = cursor.fetchone()[0]
    conn.close()
    return total_gewinn if total_gewinn else 0

@app.route('/admin')
def admin():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lottery_data")
    data = cursor.fetchall()

    gesamtgewinn = get_total_gewinn()
    conn.close()

    return render_template('admin.html', data=data, gesamtgewinn=gesamtgewinn)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def uebergangend():
    type = request.args.get('type')
    gewinn = float(request.args.get('gewinn'))
    benutztergewinn = float(request.args.get('benutztergewinn'))
    einsatz = int(request.args.get('einsatz', 3))

    return render_template(f'{type}.html', einsatz=einsatz, gewinn=gewinn, benutztergewinn=benutztergewinn)

@app.route('/uebergangend')
def uebergangend_template():
    type = request.args.get('type')
    gewinn = float(request.args.get('gewinn'))
    benutztergewinn = float(request.args.get('benutztergewinn'))
    einsatz = int(request.args.get('einsatz', 3))

    return render_template(f'{type}.html', einsatz=einsatz, gewinn=gewinn, benutztergewinn=benutztergewinn)


@app.route('/loskaufen', methods=['POST'])
def loskaufen():
    einsatz = int(request.form.get('einsatz', 3))
    geld = random.randint(1, 3)

    if random.randint(1, 3) == 1:
        if geld == 1:
            benutztergewinn = einsatz * 1.33 
            gewinn = (benutztergewinn * -1) + einsatz
            benutztergewinn = round(benutztergewinn, 2)
            gewinn = round(gewinn, 2)
            add_to_lottery_data(gewinn)
            return render_template(f'uebergang.html', type='won4', einsatz=einsatz, gewinn=gewinn, benutztergewinn=benutztergewinn)

        elif geld == 2:
            benutztergewinn = einsatz * 2
            gewinn = (benutztergewinn * -1) + einsatz
            benutztergewinn = round(benutztergewinn, 2)
            gewinn = round(gewinn, 2)
            add_to_lottery_data(gewinn)
            return render_template(f'uebergang.html', type='won6', einsatz=einsatz, gewinn=gewinn, benutztergewinn=benutztergewinn)

        else:
            benutztergewinn = einsatz * 2.66
            gewinn = (benutztergewinn * -1) + einsatz
            benutztergewinn = round(benutztergewinn, 2)
            gewinn = round(gewinn, 2)
            add_to_lottery_data(gewinn)
            return render_template(f'uebergang.html', type='won8', einsatz=einsatz, gewinn=gewinn, benutztergewinn=benutztergewinn)

    else:
        gewinn = einsatz
        add_to_lottery_data(gewinn)
        return render_template('uebergang.html', type='lost', einsatz=einsatz, gewinn=gewinn, benutztergewinn=0)

if __name__ == '__main__':
    app.run(debug=True, port=5500, host='0.0.0.0')