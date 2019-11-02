"""REST API for likes."""
import flask
import backend


@backend.app.route('/api/v1/class_description/<class_name>/', methods=["GET"])
def get_class_description(class_name):
    """Return likes on postid.

    Example:
    {
      "logname_likes_this": 1,
      "likes_count": 3,
      "postid": 1,
      "url": "/api/v1/p/1/likes/"
    }
    """
    context = {
        "student_name": 'Steven Huang',
        "course_name": class_name,
        "url": flask.request.path,
        "description": 'an introduction class on data structure and algorithm'
    }
    return flask.jsonify(**context)