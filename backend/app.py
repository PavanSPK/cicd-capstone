from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)  

@app.route("/")
def home():
    return jsonify(message="Backend is running")

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/db-status")
def db_status():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cur = conn.cursor()
        cur.execute("SELECT id, name, domain FROM employees")
        rows = cur.fetchall()
        conn.close()

        return jsonify(
            database="connected",
            count=len(rows),
            employees=[
                {"id": r[0], "name": r[1], "domain": r[2]} for r in rows
            ]
        )

    except Exception as e:
        return jsonify(database="error", message=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
