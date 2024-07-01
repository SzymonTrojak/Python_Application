import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from operations.incident import Incident

def test_incident_creation():
    incident = Incident("Accident", 1, "01.07.2023 12:00", "John Doe", (50.0, 20.0))
    assert incident.description == "Accident"
    assert incident.priorty == 1
    assert incident.time == "01.07.2023 12:00"
    assert incident.reporter == "John Doe"
    assert incident.location == (50.0, 20.0)
    assert incident.ambulance is None
