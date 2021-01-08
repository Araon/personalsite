from araon import app


if __name__ == '__main__':
    website_url = 'localhost:1233'
    app.config['SERVER_NAME'] = website_url
    app.run(debug=True)