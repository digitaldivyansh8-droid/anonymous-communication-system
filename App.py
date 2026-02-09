from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random

from database import init_db, save_message
from encryption import encrypt_message, decrypt_message

app = Flask(__name__)
socketio = SocketIO(app)

init_db()

@app.route("/")
def home():
    user_id = f"User_{random.randint(1000,9999)}"
    return render_template("index.html", user_id=user_id)

@socketio.on("send_message")
def handle_message(data):
    user = data["user"]
    plain_msg = data["message"]

    encrypted = encrypt_message(plain_msg)
    save_message(user, encrypted)

    emit("receive_message", {
        "user": user,
        "message": plain_msg
    }, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
