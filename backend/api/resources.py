"""REST API for likes."""
import flask
import backend


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

    if flask.request.method == 'POST':
        # handling the json payload and run them through simple business logic first
        raw_slots = flask.request.json['response']['slots'] # slots is an array of slot dictionaries

        slot_map = {}
        for slot in raw_slots:
            slot_map[slot['slot']] = slot['raw_value'][0]

        print(slot_map)

        class_name = slot_map['_COURSE_MAPPER_']

        # modify the json payload to construct the response
        response = flask.request.json
        response['response']['slots'].append({
                'slot': 'description',
                'raw_value': ['eecs281 is an introduction class that covers data structure and algorithms']
            })

        return flask.jsonify(**response)

    return flask.jsonify(**context)


@backend.app.route('/api/v1/course_recommendation/', methods=['GET', 'POST'])
def get_class_recommendation():
    """
    Handle the recommendation competency JSON payloads with B.L. 
    """
    return 


@backend.app.route('/api/v1/clean_bye/', methods=['GET', 'POST'])
def get_clean_goodbye():
    """
    Clean the database with user specific information
    """
    return 


@backend.app.route('/api/v1/clean_hello/', methods=['GET', 'POST'])
def get_clean_hello():
    """
    Clean the database with user specific information
    """
    return


@backend.app.route('/', methods=['GET'])
def index():
    """
    Redirect any visit to the website to the REST 

    TODO: direct to the react front end in the future 
    """
    return flask.redirect('/api/v1/course_description/')