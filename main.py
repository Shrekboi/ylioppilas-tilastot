
from flask import Flask, render_template     
import sqlite3 
from cs50 import SQL



app = Flask(__name__)

db = SQL("sqlite:///tilastot.db")



@app.route("/")
# def home():
    # cursor.execute("SELECT * FROM tilastot;")

    # rows = cursor.fetchall()

    # for row in rows:
    #     print(row)
    # return 'Data fetched successfully'
def home():
    # con = sqlite3.connect("tilastot.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("SELECT * FROM '2024' WHERE koulun_nimi='Tikkurilan lukio' ORDER BY CAST(yht AS INT) DESC ")
    # rows = cur.fetchall();

    # cur.execute("SELECT nimi FROM kokeet WHERE koe IN ('A', 'O', 'Z', 'I', 'W', 'Q', 'A5', 'O5', 'M', 'N', 'BI', 'FF', 'FY', 'HI', 'PS', 'UE', 'UO', 'ET', 'GE', 'KE', 'TE', 'YH', 'BA', 'BB', 'CA', 'CB', 'EA', 'FA', 'SA', 'PA', 'VA', 'EC', 'FC', 'SC', 'PC', 'VC', 'DC', 'IC', 'QC', 'GC', 'TC', 'L1', 'L7');")

    # exams = cur.fetchall()

    # print("ROWS ARE HERE", rows)
   

    # #print(rows[1]["A"])
    # return render_template('index.html',posts = rows, exams=exams)

    grades = db.execute("SELECT * FROM '2024' WHERE koulun_nimi='Tikkurilan lukio' ORDER BY CAST(yht AS INT) DESC")

    return render_template("index.html", posts=grades)

    




    
if __name__ == "__main__":
    app.run(debug=True)