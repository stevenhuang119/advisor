"""REST API for likes."""
import flask
import backend
from flask import request, abort

@backend.app.route('/api/v1/class_description/<class_name>/', methods=["GET"])
def get_class_description(class_name):
    """
    Return the description of a class that's being asked by the students
    """
    context = {
        "student_name": 'Steven Huang',
        "course_name": class_name,
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

    print(body)

    if '_COURSE_NAME_' in body['slots']:
        if body['state'] == "course_info":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']
            body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Response for %s info inquiry' % course 

            return flask.jsonify(body)

        elif body['state'] == "course_description":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']
            body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Response for %s description inquiry' % course 

            return flask.jsonify(body)

        elif body['state'] == "course_grade_distribution":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']
            body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Response for %s grade distribution inquiry' % course 

            return flask.jsonify(body)

        elif body['state'] == "course_prereq":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']
            body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Response for %s prereq inquiry' % course 

            return flask.jsonify(body)

    else:
        abort(500)



