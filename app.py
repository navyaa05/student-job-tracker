from flask import Flask, render_template, request, redirect
from database import get_db, init_db

app = Flask(__name__)

init_db()


@app.route("/")
def index():
    db = get_db()

    jobs = db.execute(
        "SELECT * FROM jobs ORDER BY id DESC"
    ).fetchall()

    total = db.execute(
        "SELECT COUNT(*) FROM jobs"
    ).fetchone()[0]

    applied = db.execute(
        "SELECT COUNT(*) FROM jobs WHERE status = 'Applied'"
    ).fetchone()[0]

    assessment = db.execute(
        "SELECT COUNT(*) FROM jobs WHERE status = 'Assessment'"
    ).fetchone()[0]

    interview = db.execute(
        "SELECT COUNT(*) FROM jobs WHERE status = 'Interview'"
    ).fetchone()[0]

    offer = db.execute(
        "SELECT COUNT(*) FROM jobs WHERE status = 'Offer'"
    ).fetchone()[0]

    rejected = db.execute(
        "SELECT COUNT(*) FROM jobs WHERE status = 'Rejected'"
    ).fetchone()[0]

    db.close()

    return render_template(
        "index.html",
        jobs=jobs,
        total=total,
        applied=applied,
        assessment=assessment,
        interview=interview,
        offer=offer,
        rejected=rejected
    )

@app.route("/add", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        status = request.form["status"]
        application_date = request.form["application_date"]
        job_url = request.form["job_url"]
        notes = request.form["notes"]

        db = get_db()

        db.execute(
            """
            INSERT INTO jobs
            (company, role, status, application_date, job_url, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                company,
                role,
                status,
                application_date,
                job_url,
                notes
            )
        )

        db.commit()
        db.close()

        return redirect("/")

    return render_template("add.html")
@app.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    db = get_db()

    job = db.execute(
        "SELECT * FROM jobs WHERE id = ?",
        (job_id,)
    ).fetchone()

    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        status = request.form["status"]
        application_date = request.form["application_date"]
        job_url = request.form["job_url"]
        notes = request.form["notes"]

        db.execute(
            """
            UPDATE jobs
            SET company = ?,
                role = ?,
                status = ?,
                application_date = ?,
                job_url = ?,
                notes = ?
            WHERE id = ?
            """,
            (
                company,
                role,
                status,
                application_date,
                job_url,
                notes,
                job_id
            )
        )

        db.commit()
        db.close()

        return redirect("/")

    db.close()

    return render_template("edit.html", job=job)
@app.route("/details/<int:job_id>")
def details(job_id):
    db = get_db()

    job = db.execute(
        "SELECT * FROM jobs WHERE id = ?",
        (job_id,)
    ).fetchone()

    db.close()

    return render_template("details.html", job=job)
@app.route("/delete/<int:job_id>")
def delete_job(job_id):
    db = get_db()

    db.execute(
        "DELETE FROM jobs WHERE id = ?",
        (job_id,)
    )

    db.commit()
    db.close()

    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)