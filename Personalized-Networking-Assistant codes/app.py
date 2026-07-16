from flask import Flask, render_template, request
import sqlite3

from services.topic_generator import generate_topics
from services.conversation_coach import conversation_tips
from services.event_analyzer import analyze_event
from services.profile_matcher import get_matching_users
from services.fact_checker import check_fact

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        skills = request.form["skills"]
        interests = request.form["interests"]

        conn = sqlite3.connect("networking.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users(name,email,skills,interests)
                VALUES(?,?,?,?)
                """,
                (name, email, skills, interests)
            )

            conn.commit()
            conn.close()

            return """
            <h2>✅ Registration Successful!</h2>
            <br>
            <a href="/">Go Home</a>
            """

        except sqlite3.IntegrityError:

            conn.close()

            return """
            <h2>❌ Email already exists!</h2>
            <p>Please register using another email.</p>
            <a href="/register">Try Again</a>
            """

    return render_template("register.html")


@app.route("/users")
def users():

    conn = sqlite3.connect("networking.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    conn.close()

    return render_template("users.html", users=users)


@app.route("/assistant", methods=["GET", "POST"])
def assistant():

    if request.method == "POST":

        event = request.form["event"]
        interest = request.form["interest"]
        skills = request.form["skills"]

        event_info = analyze_event(event)

        topics = generate_topics(interest)

        tips = conversation_tips()

        matches = get_matching_users(skills)

        fact = check_fact(event)

        return render_template(
            "assistant.html",
            event_info=event_info,
            topics=topics,
            tips=tips,
            matches=matches,
            fact=fact
        )

    return render_template(
        "assistant.html",
        event_info=None,
        topics=None,
        tips=None,
        matches=None,
        fact=None
    )


@app.route("/login")
def login():
    return "<h2>Login Page Coming Soon</h2>"


if __name__ == "__main__":
    app.run(debug=True)