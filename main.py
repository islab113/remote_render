from flask import Flask, Response, request
import json

app = Flask(__name__)
price = 0  # Global price variable


@app.route('/setprice', methods=['POST'])
def set_price():
    global price
    data = request.get_json()

    if not data or 'price' not in data:
        response_data = json.dumps({'error': 'Missing price'})
        return Response(response=response_data, status=400, mimetype='application/json')

    try:
        price = float(data['price'])
        response_data = json.dumps({'message': 'Price updated', 'price': price})
        return Response(response=response_data, status=200, mimetype='application/json')
    except ValueError:
        response_data = json.dumps({'error': 'Invalid price format'})
        return Response(response=response_data, status=400, mimetype='application/json')

@app.route('/getprice', methods=['GET'])
def get_price():
    global price
    return Response(str(price), mimetype="text/plain")


@app.route('/')
def index():
    return "Hello from Flask + Selenium!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
