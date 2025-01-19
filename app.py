from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

# In-memory storage for user credentials (replace with database in production)
users = {}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/handle_register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users:
        flash("Username already exists. Please choose a different one!")
        return redirect(url_for("register"))

    users[username] = password
    flash("Registration successful! You can now log in.")
    return redirect(url_for("home"))

@app.route("/handle_login", methods=["POST"])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users and users[username] == password:
        return f"Welcome, {username}!"
    else:
        flash("Invalid username or password!")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
