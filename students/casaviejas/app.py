from flask import Flask
import os

app = Flask(__name__)
student = os.getenv("STUDENT_NAME", "Anon")
hood = os.getenv("BARRIO", "Unknown")

@app.get("/")
def home():
    msg = f"Hola, I am {student} and I live in {hood}"
    with open("/var/log/app/visitas.log", "a") as f:
        f.write(msg + "\n")
    return msg

@app.get("/health")
def health():
    return {"ok": True}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)