from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "👋 Trợ lý ảo đang hoạt động!"

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('command', '')
    
    if not command:
        return jsonify({'error': 'Không có lệnh nào được gửi.'}), 400

    # 🚀 Ở bước sau bạn sẽ kết nối xử lý lệnh ở đây
    response_text = f"🧠 Tôi đã nhận được lệnh: {command}"

    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
