import flask
import backend

from flask import request, abort

@backend.app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    return flask.render_template("chatbot.html")
