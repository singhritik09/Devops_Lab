from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_json', methods=['POST'])
def receive_json():
    data = request.json 
    print("Received JSON:", data)
    return 'JSON received successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 