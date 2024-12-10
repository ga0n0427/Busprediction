from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask Server is running on port 5000!"

if __name__ == '__main__':
    # Flask 서버 실행
    app.run(host='0.0.0.0', port=5000, debug=True)
