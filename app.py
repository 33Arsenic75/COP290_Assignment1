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
from graph_nifty import main
from top_bottom_3 import top_bottom_3_helper, top_bottom_3
from datetime import date
import pandas as pd
import yfinance as yf
import json

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
    balance = 1000000


# Initialize Database within Application Context
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index_nada.html")


@app.route("/update_data")
def update_data():
    # Fetch new data and update the dynamic_data dictionary
    dic = fetch_real_time()
    return dic


def create_bought_database(user_name):
    # Adjust the path and base filename as needed
    source_path = "instance/temp.json"
    destination_path = f"instance"
    new_filename = user_name
    with open(source_path, "r") as source_file:
        data = json.load(source_file)

    # Write the content to the destination with the new filename
    with open(f"{destination_path}/{new_filename}.json", "w") as destination_file:
        json.dump(data, destination_file, indent=2)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        create_bought_database(user_name=username)
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
            session["balance"] = user.balance
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


@app.route("/profile")
def profile():
    if "user_id" in session:
        return render_template(
            "profile.html",
            username=session["username"],
        )
    else:
        return redirect(url_for("index"))


@app.route("/get_balance")
def get_balance():
    if "user_id" in session:
        username = session["username"]
        query = f"SELECT balance FROM user WHERE username = '{username}'"
        conn = sqlite3.connect(f"instance/users.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        result = result[0][0]
        return [result]
    else:
        return None


@app.route("/stock")
def stock():
    if "user_id" in session:
        company_name, price, change, percentage_change, pe_ratio = real_time_price(
            "NIFTY_50", "INDEXNSE"
        )
        svg = main("NIFTY_50", "INDEXNSE")
        return render_template(
            "stock.html",
            username=session["username"],
            price=price,
            prev=change,
            percentage_change=percentage_change,
            svg=svg,
            user_name=session["username"],
        )
    else:
        return redirect(url_for("index"))


@app.route("/stocks_list", methods=["GET", "POST"])
def stocks_list():
    return render_template("stocks_list.html")


@app.route("/stock_particular", methods=["GET", "POST"])
def stock_particular():
    stock_name = request.args.get("stock_name")
    picture, info = stock_name_info(stock_name)
    df = pd.read_csv("stock_name.csv")
    df.set_index("Company Name", inplace=True)
    stock_n = stock_name
    symbol = df.loc[stock_n, "Symbol"]
    company_name, price, change, percentage_change, pe_ratio = real_time_price(
        symbol, "NSE"
    )
    prev = get_prev_closing(symbol, "NSE")
    svg = main(symbol, "NSE")
    return render_template(
        "stock_particular.html",
        stock_name=stock_name,
        picture=picture,
        price=price,
        change=change,
        percentage_change=percentage_change,
        pe_ratio=pe_ratio,
        prev=prev,
        svg=svg,
        info=info,
        user_name=session["username"],
    )


@app.route("/get_quantity")
def stock_quantity():
    stock = request.args.get("stock")
    user = session["username"]
    file_path = f"instance/{user}.json"
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    quantity = data.get(stock)
    return [quantity]


@app.route("/BUY", methods=["POST"])
def BUY():
    data = request.json
    quantity = float(data.get("quantity"))
    price = float(data.get("price"))
    user = data.get("user")
    stock = data.get("stock")
    print(data.get("balance"))
    balance = float(data.get("balance"))

    if balance < quantity * price:
        response_data = {"message": "Not Enough Balance", "stock_quantity": data[stock]}
        return jsonify(response_data)
    else:
        query = f"UPDATE user SET balance = {balance} - {quantity*price} WHERE username = '{user}' "
        conn = sqlite3.connect(f"instance/users.db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        file_path = f"instance/{user}.json"
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        data[stock] = float(data[stock]) + quantity

        # Write the updated data back to the JSON file
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)
        response_data = {
            "message": "BOUGHT SUCCESSFULLY!",
            "stock_quantity": data[stock],
        }
        return jsonify(response_data)


@app.route("/SELL", methods=["POST"])
def SELL():
    data = request.json
    quantity = float(data.get("quantity"))
    price = float(data.get("price"))
    user = data.get("user")
    stock = data.get("stock")
    balance = float(data.get("balance"))
    file_path = f"instance/{user}.json"
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    bought = data[stock]
    if quantity > bought:
        response_data = {
            "message": "Not Enough Stocks in Balance",
            "stock_quantity": data[stock],
        }
        return jsonify(response_data)
    else:
        query = f"UPDATE user SET balance = {balance} + {quantity*price} WHERE username = '{user}' "
        conn = sqlite3.connect(f"instance/users.db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        data[stock] = float(data[stock]) - quantity
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)
        response_data = {"message": "SOLD SUCCESSFULLY!", "stock_quantity": data[stock]}
        return jsonify(response_data)


@app.route("/Profit")
def profit():
    user = ""
    if "user_id" in session:
        user = session["username"]
    file_path = f"instance/{user}.json"
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    pr = {}
    temp = {}
    for row in yester_day_data:
        temp[row[0]] = [row[1], row[2]]

    df = pd.read_csv("stock_name.csv")
    for name, symbol in zip(df["Company Name"], df["Symbol"]):
        if data[name] != 0:
            pr[name] = []
            pr[name].append(temp[symbol])
            pr[name].append(data[name])
    print(pr)
    return jsonify(pr)


@app.route("/compare_stock")
def compare_stock():
    return render_template("compare_stock.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop()
    return redirect(url_for("index"))


@app.route("/query", methods=["POST"])
def query_database():
    data = request.json  # assuming data is sent in JSON format
    startDate = data.get("startDate")
    endDate = data.get("endDate")
    stock = data.get("stock")
    query = f"SELECT DATE(DATE) as date,CLOSE FROM stock_data_table WHERE date BETWEEN '{startDate}' AND '{endDate}'"
    conn = sqlite3.connect(f"historical_data/{stock}.db")
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return jsonify(result)


@app.route("/filter")
def filter():
    return render_template("filter.html")


@app.route("/default_filter", methods=["POST"])
def default_filter():
    data = request.json
    category = data["category"]
    month = int(data["month"])
    lowerbound = float(data["lowerBound"])
    upperbound = float(data["upperBound"])
    company_name = pd.read_csv("stock_name.csv")
    result = {}
    for name in company_name["Company Name"]:
        if name == "Nifty_Fifty" or name == "Sensex":
            continue
        db_path = f"historical_data/{name}.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = f"SELECT AVG({category}) FROM stock_data_table WHERE DATE >= date('now', '-{month} months')"
        cursor.execute(query)
        average_value = cursor.fetchone()[0]
        if average_value >= lowerbound and average_value <= upperbound:
            result[name] = average_value
        conn.close()
    # print(result)
    return jsonify(result)


@app.route("/PE_filter", methods=["POST"])
def PE_filter():
    data = request.json
    month = int(data["month"])
    lowerbound = float(data["lowerBound"])
    upperbound = float(data["upperBound"])
    company_name = pd.read_csv("stock_name.csv")
    result = {}
    for row in yester_day_data:
        if row[1] >= lowerbound and row[1] <= upperbound:
            result[row[0]] = row[1]
    # print(result)
    return jsonify(result)


@app.route("/top_3")
def top_3():
    # data = top_bottom_3()
    top = data[0]
    bottom = data[1]
    dic = {}
    dic[0] = top[0]
    dic[1] = top[1]
    dic[2] = top[2]
    dic[3] = bottom[0]
    dic[4] = bottom[1]
    dic[5] = bottom[2]
    return dic


if __name__ == "__main__":
    yester_day_data = top_bottom_3_helper()
    data = top_bottom_3(yester_day_data)
    app.run(debug=True)
    # data = top_bottom_3()
