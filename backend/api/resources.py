"""REST API for likes."""
import flask
import backend


@backend.app.route('/api/v1/class_description/', methods=['GET', 'POST'])
def get_class_description(class_name):
    """
    Handle the description competency JSON payloads with B.L. 
    """
    context = {
        "student_name": 'Steven Huang',
        "course_name": class_name,
        "url": flask.request.path,
        "description": 'an introduction class on data structure and algorithm'
    }
    return flask.jsonify(**context)


@backend.app.route('/api/v1/class_recommendation/', methods=['GET', 'POST'])
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
    return flask.redirect('/api/v1/class_description/')