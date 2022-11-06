from app import app


@app.route('/book', methods=['get'])
def book():
    return 'lol'
