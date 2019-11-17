import flask
import backend
import requests

from flask import request, abort

@backend.app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():

    url1 = "https://3.133.94.198/v1/oauth/"
    #url2 = "https://3.133.104.132/v1/query/"
    #url3 = "http://3.133.104.132/v1/apps/applicationtoken/"

    # Data when using the password grant type
    payload =(
        "institution=eecs498team4",
        "&username=user6",
        "&password=password6",
        "&grant_type=password"
    )

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    print("sending payload")
    response = requests.post(url1, json=payload, headers=headers)
    print("payload received")

    print(response.json())

    return flask.render_template("chatbot.html", response)


