"""REST API for likes."""
import flask
import backend
from flask import request, abort

@backend.app.route('/api/v1/course_description/', methods=['GET', 'POST'])
def get_class_description():
    """
    Handle the description competency JSON payloads with B.L. 
    """
    context = {
        "response": "this is the response of a get request, you should not see this",
        "student_name": 'Steven Huang',
        "course_name": 281,
        "url": flask.request.path,
        "description": 'an introduction class on data structure and algorithm'
    }
    return flask.jsonify(**context)

@backend.app.route('/webhook_test', methods=['GET','POST'])
def webhook_test():
    if request.method == 'POST':
        print(request.json)
        return '', 200

    else:
        abort(400)

@backend.app.route('/api/v1/advisor_webhook', methods=['POST'])
def advisor_webhook(): 
    
    body = request.json

    if body['state'] == "course_info":
        body['slots']['course_name']['values'][0]['resolved'] = 1
        body['slots']['course_name']['values'][0]['value'] = "Response for course info inquiry" 

        return flask.jsonify(body)

    elif body['state'] == "course_description":
        body['slots']['course_name']['values'][0]['resolved'] = 1
        body['slots']['course_name']['values'][0]['value'] = "Response for course description inquiry" 

        return flask.jsonify(body)

    elif body['state'] == "course_grade_distribution":
        body['slots']['course_name']['values'][0]['resolved'] = 1
        body['slots']['course_name']['values'][0]['value'] = "Response for course grade distribution inquiry" 

        return flask.jsonify(body)

    elif body['state'] == "course_prereq":
        body['slots']['course_name']['values'][0]['resolved'] = 1
        body['slots']['course_name']['values'][0]['value'] = "Response for course prereq inquiry" 


        return flask.jsonify(body)

    else:
        abort(500)



