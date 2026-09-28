"""Implements the settings webpage."""

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

    for config_path in control_path.glob("*.ctl"):
        # Try loading the control config.
        config = controls.ControlConfig.parse_from_file(str(config_path))

        if config.is_valid() == False:
            continue

    return flask.render_template("settings.html", controls={})
