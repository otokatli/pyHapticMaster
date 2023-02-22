from haptic_master.haptic_master import HapticMaster
from haptic_master.effect import Spring
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_block(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()

    def test_sphere(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()

    def test_flat_plane(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()

    def test_cylinder(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()

    def test_torus(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()

        
if __name__ == '__main__':
    unittest.main()