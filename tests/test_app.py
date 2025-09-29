import os
import sys
import pytest
from dash.testing.application_runners import import_app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture
def app_runner(dash_duo):
    os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"
    app = import_app("app")
    dash_duo.start_server(app)
    return dash_duo

def test_header_present(app_runner):
    header = app_runner.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"

def test_chart_present(app_runner):
    chart = app_runner.find_element("#sales-chart")
    assert chart is not None

def test_region_picker_present(app_runner):
    picker = app_runner.find_element("#region-filter")
    assert picker is not None
