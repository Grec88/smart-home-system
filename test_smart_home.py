import unittest
from smart_home import Light

class TestLight(unittest.TestCase):
    def test_turn_on_light(self):
        light = Light()
        result = light.turn_on()
        self.assertTrue(light.is_on)
        self.assertEqual(result, "Light turned on")

    def test_turn_on_already_on_light(self):
        light = Light()
        light.turn_on()
        result = light.turn_on()
        self.assertTrue(light.is_on)
        self.assertEqual(result, "Light is already on")

    def test_turn_off_light(self):
        light = Light()
        light.turn_on()
        result = light.turn_off()
        self.assertFalse(light.is_on)
        self.assertEqual(result, "Light turned off")

    def test_turn_off_already_off_light(self):
        light = Light()
        result = light.turn_off()
        self.assertFalse(light.is_on)
        self.assertEqual(result, "Light is already off")

if __name__ == '__main__':
    unittest.main()