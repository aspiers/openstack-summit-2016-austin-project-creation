#!/usr/bin/python2


from flask import Flask, send_from_directory
import os


DEBUG = False
PORT = 55555
PATH = os.path.abspath('.')
print("Your ppt is here: localhost:55555/austin-talk/index.html")


def display_ppt(PATH):
    app = Flask(__name__, static_url_path='')
    html_path = PATH

    @app.route('/austin-talk/<path:path>')
    def presentation(path):
        return send_from_directory(html_path, path)

    app.run(host='127.0.0.1', port=PORT, debug=DEBUG)


if __name__ == "__main__":

    display_ppt(PATH)
