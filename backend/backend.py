import json
from flask import Flask
import sys
import socket

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "<html><body>This is {0}</body></html>".format(socket.gethostname())

app.run(host="0.0.0.0", port=sys.argv[1])