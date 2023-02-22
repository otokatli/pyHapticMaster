from haptic_master.haptic_master import HapticMaster
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_shaker(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()

        
if __name__ == '__main__':
    unittest.main()