from light import Light
from climate import ClimateControl

def test_light():
    light = Light("Living Room")
    assert light.turn_on() == "Living Room light turned on"
    assert light.turn_off() == "Living Room light turned off"

def test_climate():
    climate = ClimateControl("Bedroom", 23, 45)
    climate.update_conditions(21, 40)
    assert climate.heater_on is True
    assert climate.humidifier_on is True

test_light()
test_climate()
