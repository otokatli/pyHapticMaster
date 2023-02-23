from haptic_master.haptic_master import HapticMaster
from haptic_master.shaker import Shaker
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_shaker(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        frequency1 = 0.21
        frequency2 = 0.12
        direction = [0.0, 1.0, 0.0]
        posmax = 0.23
        velmax = 2.3
        accmax = 23.0
        stiffness = 120.0
        dampfactor = 0.02
        deadband = 1.3
        maxforce = 12.5

        my_shaker = Shaker('my_shaker', robot)

        self.assertTrue(my_shaker.create())

        self.assertTrue(my_shaker.set_frequency1(frequency1))
        self.assertEqual(my_shaker.get_frequency1(), frequency1)

        self.assertTrue(my_shaker.set_frequency2(frequency2))
        self.assertEqual(my_shaker.get_frequency2(), frequency2)

        self.assertTrue(my_shaker.set_direction(direction))
        self.assertEqual(my_shaker.get_direction(), direction)

        self.assertTrue(my_shaker.set_posmax(posmax))
        self.assertEqual(my_shaker.get_posmax(), posmax)

        self.assertTrue(my_shaker.set_velmax(velmax))
        self.assertEqual(my_shaker.get_velmax(), velmax)

        self.assertTrue(my_shaker.set_accmax(accmax))
        self.assertEqual(my_shaker.get_accmax(), accmax)

        self.assertTrue(my_shaker.set_stiffness(stiffness))
        self.assertEqual(my_shaker.get_stiffness(), stiffness)

        self.assertTrue(my_shaker.set_dampfactor(dampfactor))
        self.assertEqual(my_shaker.get_dampfactor(), dampfactor)

        self.assertTrue(my_shaker.set_deadband(deadband))
        self.assertEqual(my_shaker.get_deadband(), deadband)

        self.assertTrue(my_shaker.set_maxforce(maxforce))
        self.assertEqual(my_shaker.get_maxforce(), maxforce)

        robot.disconnect()


if __name__ == '__main__':
    unittest.main()
