import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    uid = session["user_id"]

    usable = db.execute(
        "SELECT symbol, name, price, SUM(shares) as Tshares FROM trans WHERE user_id = ? GROUP BY symbol", uid)
    money = db.execute(
        "SELECT cash FROM users WHERE id = ?", uid)[0]["cash"]

    TOTAL = money
    for i in usable:
        TOTAL += i["price"] * i["Tshares"]

    return render_template("index.html", stock=usable, cash=money, usd=usd, total=TOTAL)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        namad = request.form.get("symbol").upper()
        item = lookup(namad)
        if not namad:
            return apology("Empty!!!",400)
        elif not item:
            return apology("namotabar!!!",400)

        try:
            sahm = int(request.form.get("shares"))
        except:
            return apology("Enter enteger!!!",400)

        if sahm < 1:
            return apology("Enter positive!!!",400)

        uid = session["user_id"]
        money = db.execute("SELECT cash FROM users WHERE id = ?", uid)[0]["cash"]

        itp = item["price"]
        itn = item["name"]
        totp = itp * sahm

        if money < totp:
            return apology("out of stock!!!",400)
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", money - totp, uid)
            db.execute("INSERT INTO trans (user_id, name, shares, price, type, symbol) VALUES(?, ?, ?, ?, ?, ?)",
                       uid, itn, sahm, itp, 'buy', namad)

        return redirect('/')
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    uid = session["user_id"]
    tr = db.execute("SELECT type, symbol, price, shares, time FROM trans WHERE user_id = ?", uid)

    return render_template("history.html", trans=tr, usd=usd)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        namad = request.form.get('symbol')
        if not namad:
            return apology("invalid!!!",400)

        usable = lookup(namad)
        if not usable:
            return apology("invalid!!!",400)

        return render_template("quoted.html", stock=usable, uf=usd)

    else:
        return render_template('quote.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if (request.method == "POST"):
        un = request.form.get('username')
        pas = request.form.get('password')
        verification = request.form.get('confirmation')

        if not un:
            return apology("username Empty!!!",400)
        elif not pas:
            return apology('Password empty!!!',400)
        elif not verification:
            return apology('notconfirm your password!',400)

        if pas != verification:
            return apology('false')

        hash = generate_password_hash(pas)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", un, hash)
            return redirect('/')
        except:
            return apology('!!!used before!!!')
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    uid = session["user_id"]
    if request.method == "POST":
        namad = request.form.get("symbol")
        saham = int(request.form.get("shares"))
        if saham < 1:
            return apology("!enter positive number!")
        itp = lookup(namad)["price"]
        itn = lookup(namad)["name"]
        pr = saham * itp

        sma = db.execute("SELECT shares FROM trans WHERE user_id = ? AND symbol = ? GROUP BY symbol", uid, namad)[0]["shares"]

        if sma < saham:
            return apology("out of stock!")

        smb = db.execute("SELECT cash FROM users WHERE id = ?", uid)[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", smb + pr, uid)
        db.execute("INSERT INTO trans (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)",
                   uid, itn, -saham, itp, "sell", namad)

        return redirect('/')
    else:
        nama = db.execute("SELECT symbol FROM trans WHERE user_id = ? GROUP BY symbol", uid)
        return render_template("sell.html", symbols=nama)





