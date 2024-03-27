from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    
    return jsonify({'student_number': '200583712'}), 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
   
    return jsonify({
        'fulfillmentText': 'Thank you and have a nice day!'
    })

if __name__ == '__main__':
    app.run(debug=True)

