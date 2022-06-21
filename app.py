#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/api/v0.1/recipes')
def index():
	return 'hello, World!'

if __name__ == '__main__':
	app.run(debug=True)