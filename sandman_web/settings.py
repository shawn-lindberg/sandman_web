"""Implements the settings webpage."""

import flask

blueprint = flask.Blueprint("settings", __name__, template_folder="templates")


@blueprint.route("/settings")
def home() -> str:
    """Implement the route for the settings page."""
    return flask.render_template("settings.html", controls={})
