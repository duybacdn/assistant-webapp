from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🎉 Assistant đã sẵn sàng nhận lệnh!"

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    command_text = data.get("command", "")
    return jsonify({"response": f"Bạn vừa gửi: {command_text}"})

# Chạy thử tại localhost
if __name__ == "__main__":
    app.run(debug=True)
