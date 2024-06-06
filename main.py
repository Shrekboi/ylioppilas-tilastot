from flask import Flask, render_template, request, flash
from cs50 import SQL

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQL("sqlite:///tilastot.db")

@app.route("/")
def home():
    # cur.execute("SELECT * FROM '2024' WHERE koulun_nimi='Tikkurilan lukio' ORDER BY CAST(yht AS INT) DESC ")

    # cur.execute("SELECT nimi FROM kokeet WHERE koe IN ('A', 'O', 'Z', 'I', 'W', 'Q', 'A5', 'O5', 'M', 'N', 'BI', 'FF', 'FY', 'HI', 'PS', 'UE', 'UO', 'ET', 'GE', 'KE', 'TE', 'YH', 'BA', 'BB', 'CA', 'CB', 'EA', 'FA', 'SA', 'PA', 'VA', 'EC', 'FC', 'SC', 'PC', 'VC', 'DC', 'IC', 'QC', 'GC', 'TC', 'L1', 'L7');")


    searchLukio = request.args.get("lukio")

    if searchLukio == "":
        grades = db.execute("SELECT * FROM '2024' ORDER BY CAST(yht AS INT) DESC LIMIT 1000")
    else:
        grades = db.execute("SELECT * FROM '2024' WHERE koulun_nimi=? ORDER BY CAST(yht AS INT) DESC", searchLukio)

    return render_template("index.html", posts=grades)


@app.route("/top100")
def best():
    top100 = db.execute("SELECT * FROM '2024' ORDER BY CAST(yht AS INT) DESC LIMIT 100")

    flash("SHALOOM")
    return render_template("index.html", posts=top100)


@app.route("/info")
def get_info():
    sid = request.args.get("pupil_id")

    student_info = db.execute("SELECT * FROM '2024' WHERE random_id = ?", sid)

    exam_names = db.execute("SELECT nimi FROM kokeet WHERE koe IN ('A', 'O', 'Z', 'I', 'W', 'Q', 'A5', 'O5', 'M', 'N', 'BI', 'FF', 'FY', 'HI', 'PS', 'UE', 'UO', 'ET', 'GE', 'KE', 'TE', 'YH', 'BA', 'BB', 'CA', 'CB', 'EA', 'FA', 'SA', 'PA', 'VA', 'EC', 'FC', 'SC', 'PC', 'VC', 'DC', 'IC', 'QC', 'GC', 'TC', 'L1', 'L7');")
    exam_id = db.execute("SELECT koe, nimi FROM kokeet;")
    return render_template("student_info.html", data= student_info, exams=exam_names, ids=exam_id)


if __name__ == "__main__":
    app.run(debug=True)
