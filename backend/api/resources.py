"""REST API for likes."""
import flask
import backend
import pandas as pd
from flask import request, abort


class_data = pd.read_csv('backend/api/coursework.csv')
class_data.set_index('Course', inplace=True)
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

def drop_old_resolved_for_new(body):
    to_delete_indices = []
    num_resolved = 0
    if len(body['slots']['_COURSE_NAME_']['values']) == 1:
        return
    for i in range(len(body['slots']['_COURSE_NAME_']['values'])):
        if body['slots']['_COURSE_NAME_']['values'][i]['resolved'] == 1:
            to_delete_indices.append(i)
        if body['slots']['_COURSE_NAME_']['values'][i]['resolved'] == -1 and num_resolved == 0:
            num_resolved += 1
            body['slots']['_COURSE_NAME_']['values'][i]['resolved'] == 1

    for index in to_delete_indices:
        del body['slots']['_COURSE_NAME_']['values'][index]


@backend.app.route('/api/v1/advisor_webhook', methods=['POST'])
def advisor_webhook(): 
    body = request.json
    
    print('---------STARTING RESPONSE CODE---------------')
    print(body)

    if '_COURSE_NAME_' in body['slots']:
        drop_old_resolved_for_new(body)
        if body['state'] == "course_info":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']

            if course in class_data.index:
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'What would you like to know about %s?' % course     

            else:
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Sorry, class does not exist' 

            return flask.jsonify(body)

        elif body['state'] == "course_description":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']

            if course in class_data.index: 
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'The description for ' + course + ' is the following: ' + class_data.loc[course]['Description']

            else:
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Sorry, class does not exist' 

            return flask.jsonify(body)

        elif body['state'] == "course_grade_distribution":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']
            
            if course in class_data.index: 
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'The average grade for ' + course + ' is ' + class_data.loc[course]['Median Grade']

            else:
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Sorry, class does not exist' 

            return flask.jsonify(body)


        elif body['state'] == "course_prereq":
            body['slots']['_COURSE_NAME_']['values'][0]['resolved'] = 1
            course = body['slots']['_COURSE_NAME_']['values'][0]['course_mapper']
            
            if course in class_data.index: 
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'The prerequisites for ' + course + ' are the following: ' + class_data.loc[course]['Prerequisites']     

            else:
                body['slots']['_COURSE_NAME_']['values'][0]['value'] = 'Sorry, class does not exist' 

            return flask.jsonify(body)

    elif body['state'] == 'course_recommendation':
        
        if '_COURSE_CRITERIA_' in body['slots']:
            
            body['slots']['_COURSE_CRITERIA_']['values'][0]['resolved'] = 1
            topic = body['slots']['_COURSE_CRITERIA_']['values'][0]['course_mapper']
            
            if topic == "Artificial Intelligence":
                body['slots']['_COURSE_CRITERIA_']['values'][0]['value'] = 'You should look to take EECS 492, Artificial Intelligence.'

            elif topic == "Machine Learning":
                body['slots']['_COURSE_CRITERIA_']['values'][0]['value'] = 'You should look to take EECS 445, Machine Learning.'

            elif topic == "Web Development":
                body['slots']['_COURSE_CRITERIA_']['values'][0]['value'] = 'You should look to take EECS 485, Web Systems, for full-stack development. EECS 484, Database Management Systems, will also give you backend knowledge. EECS 493, User Interface Development, will give you frontend experience.'

            elif topic == "MDE":
                body['slots']['_COURSE_CRITERIA_']['values'][0]['value'] = 'Popular capstone/mde courses include EECS 497, Human-Centered Software and Design and Development, and EECS 441, Mobile App Development for Entrepreneurs. For a great special topics MDE course, check out EECS 498 Conversational AI'

            else:
                body['slots']['_COURSE_CRITERIA_']['values'][0]['value'] = 'Sorry, I have no recommendation for you at this time. I could an issue with my mapper, or it could be that I am not trained to recommend in your requested area.'

            return flask.jsonify(body)
        else:
            body['slots']['_COURSE_CRITERIA_'] = {
                'type': 'string',
                'values': [
                    {
                        'tokens': '',
                        'resolved': 1,
                        'value': 'This is the default recommendation from an injected slot'
                    }
                ]
            }
            return flask.jsonify(body)
        # else:
        #     insert slot with default message here
             


    else:
        abort(500)
