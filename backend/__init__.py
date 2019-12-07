"""
advisor package initializer.
"""
import flask
from flask_bootstrap import Bootstrap 

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__, static_folder="static", template_folder="templates")  # pylint: disable=invalid-name

Bootstrap(app)

app.config.from_object('backend.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/config/
app.config.from_envvar('backend_SETTINGS', silent=True)

MASTER_DIALOG_TOKEN = '40C0QYWuywZbF3AwFNNohraKgX8MotY'

# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
import backend.api  # noqa: E402  pylint: disable=wrong-import-position
import backend.views 
