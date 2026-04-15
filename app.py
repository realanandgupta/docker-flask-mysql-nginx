from flask import Flask, jsonify
import pymysql

app = Flask(__name__)   # 🔥 IMPORTANT

def connect_db():
    return pymysql.connect(
        host="db",
        user="root",
        password="root",
        database="test"
    )

@app.route('/')
def home():
    return jsonify({"message": "Hello from Dockerized Flask API!"})

@app.route('/db')
def db_check():
    try:
        conn = connect_db()
        return {"message": "DB Connected!"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
