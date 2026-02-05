from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "dev-secret-change-me"  # intentionally simple for the playground

DB_PATH = os.path.join(os.path.dirname(__file__), "app.db")


def get_db():
    """Open a new database connection per request."""
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def current_user():
    """Return the currently logged in user row or None."""
    uid = session.get("user_id")
    if not uid:
        return None
    db = get_db()
    return db.execute("SELECT id, username, email FROM users WHERE id = ?", (uid,)).fetchone()


@app.route("/")
def index():
    user = current_user()
    return render_template("index.html", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    INTENTIONALLY VULNERABLE: SQL Injection
    This login uses string concatenation instead of parameterized queries.
    """
    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # ❌ Vulnerable on purpose (SQL Injection)
        query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"
        db = get_db()
        user = db.execute(query).fetchone()

        if user:
            session["user_id"] = int(user["id"])
            return redirect(url_for("index"))
        else:
            error = "Invalid credentials."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/profile")
def profile():
    """
    INTENTIONALLY VULNERABLE: IDOR
    Missing authorization checks. Any logged-in user can access any profile by changing ?id=
    Example: /profile?id=2
    """
    if not session.get("user_id"):
        return redirect(url_for("login"))

    requested_id = request.args.get("id", "")
    if not requested_id:
        requested_id = str(session["user_id"])  # default: own profile

    db = get_db()
    user = db.execute(
        "SELECT id, username, email FROM users WHERE id = ?",
        (requested_id,),
    ).fetchone()

    if not user:
        return "User not found", 404

    return render_template("profile.html", user=user, requested_id=requested_id)


@app.route("/comments", methods=["GET", "POST"])
def comments():
    """
    INTENTIONALLY VULNERABLE: Stored XSS
    - Stores user-provided comment content
    - Renders it back unsafely (see template using |safe)
    """
    if not session.get("user_id"):
        return redirect(url_for("login"))

    db = get_db()
    user = current_user()

    if request.method == "POST":
        content = request.form.get("content", "")

        # ❌ Vulnerable on purpose: store raw input without sanitization
        db.execute(
            "INSERT INTO comments (user_id, content) VALUES (?, ?)",
            (user["id"], content),
        )
        db.commit()
        return redirect(url_for("comments"))

    rows = db.execute(
        """
        SELECT c.id, c.content, c.user_id, u.username
        FROM comments c
        JOIN users u ON u.id = c.user_id
        ORDER BY c.id DESC
        """
    ).fetchall()

    return render_template("comments.html", user=user, comments=rows)


if __name__ == "__main__":
    # Debug on purpose (local lab only)
    app.run(debug=True)