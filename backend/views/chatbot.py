import flask
import backend

from flask import request, abort, jsonify

@backend.app.route('/chatbot/', methods=['GET', 'POST'])
def chatbot():
    return flask.render_template("chatbot.html")

@backend.app.route('/_clinc_process')
def clinc_process():
    try:
        text =  request.args.get('text', 0, type=str)

        return jsonify(result = text + " (this is response)")


    except Exception as e:
        return str(e)
