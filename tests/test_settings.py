"""Tests the settings page."""

import flask
import flask.testing


def test_settings(client: flask.testing.FlaskClient) -> None:
    """Test the settings page."""
    assert client.get("/settings").status_code == 200
