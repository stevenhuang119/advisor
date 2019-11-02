"""REST API for likes."""
import flask
import backend


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