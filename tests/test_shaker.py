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

        myShaker = Shaker('myShaker', robot)
        
        self.assertTrue(myShaker.create())

        self.assertTrue(myShaker.set_frequency1(frequency1))
        self.assertEqual(myShaker.get_frequency1(), frequency1)
        
        self.assertTrue(myShaker.set_frequency2(frequency2))
        self.assertEqual(myShaker.get_frequency2(), frequency2)
        
        self.assertTrue(myShaker.set_direction(direction))
        self.assertEqual(myShaker.get_direction(), direction)
        
        self.assertTrue(myShaker.set_posmax(posmax))
        self.assertEqual(myShaker.get_posmax(), posmax)
        
        self.assertTrue(myShaker.set_velmax(velmax))
        self.assertEqual(myShaker.get_velmax(), velmax)
        
        self.assertTrue(myShaker.set_accmax(accmax))
        self.assertEqual(myShaker.get_accmax(), accmax)
        
        self.assertTrue(myShaker.set_stiffness(stiffness))
        self.assertEqual(myShaker.get_stiffness(), stiffness)
        
        self.assertTrue(myShaker.set_dampfactor(dampfactor))
        self.assertEqual(myShaker.get_dampfactor(), dampfactor)
        
        self.assertTrue(myShaker.set_deadband(deadband))
        self.assertEqual(myShaker.get_deadband(), deadband)
        
        self.assertTrue(myShaker.set_maxforce(maxforce))
        self.assertEqual(myShaker.get_maxforce(), maxforce)

        robot.disconnect()

        
if __name__ == '__main__':
    unittest.main()