"""falsk starter."""
from flask import Flask, render_template
WSGI_APLLICATION = Flask(__name__)
WSGI_APLLICATION.config['TEMPLATES_AUTO_RELOAD'] = True
@WSGI_APLLICATION.route('/')
def hello_world():
    """renders template."""
    return render_template('index.html')

if __name__ == '__main__':
    WSGI_APLLICATION.run(debug=True, port=8080)
