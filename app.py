from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from real_time_price import real_time_price, fetch_real_time, get_prev_closing
from information import stock_name_info
import sqlite3
import pandas as pd

app = Flask(__name__, static_url_path="/static")
app.secret_key = "1234"  # Replace with your actual secret key

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)


# Initialize Database within Application Context
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index_nada.html")


@app.route("/update_data")
def update_data():
    # Fetch new data and update the dynamic_data dictionary
    dict = fetch_real_time()
    return dict


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.")
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password")
            return redirect(url_for("index"))
    else:
        return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        company_name, price, change, percentage_change, pe_ratio = real_time_price(
            "NIFTY_50", "INDEXNSE"
        )
        return render_template(
            "welcome_nada.html",
            username=session["username"],
            price=price,
            prev=change,
            percentage_change=percentage_change,
        )
    else:
        return redirect(url_for("index"))


@app.route("/stock")
def stock():
    if "user_id" in session:
        company_name, price, change, percentage_change, pe_ratio = real_time_price(
            "NIFTY_50", "INDEXNSE"
        )
        return render_template(
            "stock.html",
            username=session["username"],
            price=price,
            prev=change,
            percentage_change=percentage_change,
        )
    else:
        return redirect(url_for("index"))


@app.route("/stocks_list", methods=["GET", "POST"])
def stocks_list():
    return render_template("stocks_list.html")


@app.route("/stock_particular", methods=["GET", "POST"])
def stock_particular():
    stock_name = request.args.get("stock_name")
    picture = stock_name_info(stock_name)
    df = pd.read_csv("stock_name.csv")
    df.set_index("Company Name", inplace=True)
    stock_n = stock_name
    symbol = df.loc[stock_n, "Symbol"]
    company_name, price, change, percentage_change, pe_ratio = real_time_price(
        symbol, "NSE"
    )
    prev = get_prev_closing(symbol, "NSE")
    return render_template(
        "stock_particular.html",
        stock_name=stock_name,
        picture=picture,
        price=price,
        change=change,
        percentage_change=percentage_change,
        pe_ratio=pe_ratio,
        prev=prev,
    )


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/query", methods=["POST"])
def query_database():
    data = request.json  # assuming data is sent in JSON format
    startDate = data.get("startDate")
    endDate = data.get("endDate")
    stock = data.get("stock")
    query = f"SELECT DATE(DATE) as date,CLOSE FROM stock_data_table WHERE date BETWEEN {startDate} AND {endDate}"
    # Connect to the database (SQLite in this example)
    conn = sqlite3.connect(f"historical_data/{stock}")
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)
    result = cursor.fetchall()

    # Close the database connection
    conn.close()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
