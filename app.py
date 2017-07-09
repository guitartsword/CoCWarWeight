"""flask starter."""
from flask import Flask, render_template, send_from_directory
WSGI_APLLICATION = Flask(__name__)
WSGI_APLLICATION.config['TEMPLATES_AUTO_RELOAD'] = True
@WSGI_APLLICATION.route('/<path>')
@WSGI_APLLICATION.route('/')
def hello_world(path=''):
    """renders template."""
    return render_template('index.html')
if __name__ == '__main__':
    WSGI_APLLICATION.run(host='0.0.0.0', debug=True, port=8080)
