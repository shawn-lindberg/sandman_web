"""Implements the settings webpage."""

import operator
import pathlib

import flask
import sandman_core.controls as controls

blueprint = flask.Blueprint(
    "settings",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@blueprint.route("/settings")
def home() -> str:
    """Implement the route for the settings page."""
    control_path = pathlib.Path(
        str(flask.current_app.config["BASE_DIR"]) + "/controls"
    )

    # Make a list of control configurations.
    unsorted_controls = []

    for config_path in control_path.glob("*.ctl"):
        # Try loading the control config.
        config = controls.ControlConfig.parse_from_file(str(config_path))

        if config.is_valid() == False:
            continue

        unsorted_controls.append(config.get_as_json())

    # Sort them by name.
    sorted_controls = sorted(
        unsorted_controls, key=operator.itemgetter("name")
    )

    return flask.render_template("settings.html", controls=sorted_controls)
