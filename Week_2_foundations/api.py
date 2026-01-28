from flask import Flask, jsonify
import pandas as pd
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("sales.db", check_same_thread=False)
df = pd.read_sql("SELECT * FROM sales", conn)

@app.route("/")
def home():
    return "Sales API is running"

@app.route("/sales")
def all_sales():
    return jsonify(df.to_dict(orient="records"))

@app.route("/sales/<city>")
def sales_by_city(city):
    data = df[df["city"].str.lower() == city.lower()]
    return jsonify(data.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
