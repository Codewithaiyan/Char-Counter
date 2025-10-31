from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/count', methods=['POST'])
def count_characters():
    try:
        data = request.get_json()
        name = data.get('name', '')
        
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        
        char_count = len(name)
        result = f"Name: {name}, Character Count: {char_count}"
        
        print(result)  # Print to stdout
        return jsonify({'result': result, 'count': char_count}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
