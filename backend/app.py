from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# ---------------------------
# Basic endpoints
# ---------------------------

@app.route("/")
def home():
    return jsonify(message="Backend is running")

@app.route("/health")
def health():
    return {"status": "ok"}, 200

# ---------------------------
# Database status endpoint
# ---------------------------

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
        cur.execute("SELECT id, name, domain FROM employees;")
        rows = cur.fetchall()

        employees = []
        for row in rows:
            employees.append({
                "id": row[0],
                "name": row[1],
                "domain": row[2]
            })

        cur.close()
        conn.close()

        return jsonify({
            "database": "connected",
            "count": len(employees),
            "employees": employees
        })

    except Exception as e:
        return jsonify({
            "database": "error",
            "message": str(e)
        }), 500

# ---------------------------
# App start
# ---------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
