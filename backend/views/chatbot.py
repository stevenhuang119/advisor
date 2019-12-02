import flask
import backend
import requests

from flask import request, abort, jsonify

@backend.app.route('/chatbot/', methods=['GET', 'POST'])
def chatbot():
    return flask.render_template("chatbot.html")

@backend.app.route('/_clinc_process')
def clinc_process():
    try:
        text =  request.args.get('text', 0, type=str)

        url = "https://api.clinc.ai/v1/query/"

        payload = {
            "query": text,
            "language": "en",
            "device": "Alexa",
            "lat": 42.2810237,
            "lon": -83.7467534,
            "time_offset": 300,
            "dialog": "40C0QYWuywZbF3AwFNNohraKgX8MotY"
        }

        headers = {
            "Authorization": "app-key da5d9c7c2209566a349ff7ba2d74b530411bcfab",
            "Content-Type": "application/json"
        }

        resp = requests.post(url, json=payload, headers=headers)

        print(resp.json())

        dept = "null"
        course = "null"

        if resp.json()['response']['slots']:
            course_ret = resp.json()['response']['slots'][0]['raw_value']['values'][0]['course_mapper']
            course_ar = course_ret.split()
            dept = course_ar[0]
            course = course_ar[1]


        ret = resp.json()['visuals']['formattedResponse']

        return jsonify(result = ret, dept = dept, course = course)


    except Exception as e:
        return str(e)


