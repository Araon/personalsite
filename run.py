from araon import app


if __name__ == '__main__':
    app.config['SERVER_NAME'] = 'localhost:5000'
    app.run(debug=True)