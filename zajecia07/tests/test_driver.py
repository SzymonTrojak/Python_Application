import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from personnel.driver import Driver

def test_driver_creation():
    driver = Driver("Jane", "Doe", 6000, "LIC1234", ["BLS"])
    assert driver.first_name == "Jane"
    assert driver.last_name == "Doe"
    assert driver.salary == 6000
    assert driver.license_number == "LIC1234"
    assert driver.qualifications == ["BLS"]

def test_display_info(caplog):
    driver = Driver("Jane", "Doe", 6000, "LIC1234", ["BLS"])
    info = driver.display_info()
    assert "Driver ID:" in info
    assert "Jane Doe" in info
