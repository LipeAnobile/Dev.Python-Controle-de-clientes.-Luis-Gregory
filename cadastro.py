from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="Trabalho",
    user="postgres",
    password="123456",
    host="localhost"
)

@app.route('/')
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM maintenances")
    maintenances = cur.fetchall()
    cur.close()
    return render_template('index.html', maintenances=maintenances)

@app.route('/register', methods=['POST'])
def register():
    date = request.form['date']
    service = request.form['service']
    notes = request.form['notes']
    
    cur = conn.cursor()
    cur.execute("INSERT INTO maintenances (date, service, notes) VALUES (%s, %s, %s)", (date, service, notes))
    conn.commit()
    cur.close()
    
    return redirect(url_for('index'))

@app.route('/edit/<int:maintenance_id>', methods=['GET', 'POST'])
def edit(maintenance_id):
    if request.method == 'POST':
        new_date = request.form['date']
        new_service = request.form['service']
        new_notes = request.form['notes']
        
        cur = conn.cursor()
        cur.execute("UPDATE maintenances SET date = %s, service = %s, notes = %s WHERE id = %s", (new_date, new_service, new_notes, maintenance_id))
        conn.commit()
        cur.close()
        
        return redirect(url_for('index'))
    else:
        cur = conn.cursor()
        cur.execute("SELECT * FROM maintenances WHERE id = %s", (maintenance_id,))
        maintenance = cur.fetchone()
        cur.close()
        
        return render_template('edit.html', maintenance=maintenance)

@app.route('/delete/<int:maintenance_id>', methods=['POST'])
def delete(maintenance_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM maintenances WHERE id = %s", (maintenance_id,))
    conn.commit()
    cur.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

