
from flask import Flask, render_template     
import sqlite3 



app = Flask(__name__)

@app.route("/")
# def home():
    # cursor.execute("SELECT * FROM tilastot;")

    # rows = cursor.fetchall()

    # for row in rows:
    #     print(row)
    # return 'Data fetched successfully'
def home():
    con = sqlite3.connect("tilastot.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM tilastot LIMIT 10")
    rows = cur.fetchall();
    return render_template('index.html',posts = rows)

    




    
if __name__ == "__main__":
    app.run(debug=True)