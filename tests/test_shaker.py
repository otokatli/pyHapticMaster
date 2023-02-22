from haptic_master.haptic_master import HapticMaster
from haptic_master.effect import Spring
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_shaker(self):
        # Open connection and set inertia to 1.0
        robot = HapticMaster(IP, PORT, 1.0)
        robot.connect()

        robot.disconnect()

        
if __name__ == '__main__':
    unittest.main()