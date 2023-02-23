from haptic_master.haptic_master import HapticMaster
from haptic_master.effect import BiasForce, Damper, Spring
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_spring(self):
        '''
        Testing the spring effect
        '''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Spring parameters
        position = [0.0, 0.2, 0.5]
        velocity = [0.0001, 0.0002, 0.0003]
        attitude = [0.0, 0.0, 0.0499792, 0.9987503]
        stiffness = 10.0
        dampfactor = 0.01
        deadband = 0.023
        direction = [1.0, 0.0, 0.0]
        maxforce = 24.2
        dampglobal = False

        # Create a spring instance
        mySpring = Spring(name='mySpring', robot=robot)

        # Create the spring on the HapticMaster controller
        self.assertTrue(mySpring.create())

        # Set position of the spring and read it from the robot
        self.assertTrue(mySpring.set_pos(position))
        self.assertEqual(mySpring.get_pos(), position)

        # Set velocity of the spring and read it from the robot
        self.assertTrue(mySpring.set_vel(velocity))
        self.assertEqual(mySpring.get_vel(), velocity)

        # Set attitude of the spring and read it from the robot
        self.assertTrue(mySpring.set_att(attitude))
        # self.assertAlmostEqual(mySpring.get_att(), attitude, places=5)

        # Enable the spring
        self.assertTrue(mySpring.set_enable())
        self.assertEqual(mySpring.get_enabled(), True)

        # Disable the spring
        self.assertTrue(mySpring.set_disable())
        self.assertEqual(mySpring.get_enabled(), False)

        # Set stiffness and read it from the robot
        self.assertTrue(mySpring.set_stiffness(stiffness))
        self.assertEqual(mySpring.get_stiffness(), stiffness)

        # # Set damping factor and read it from the robot
        self.assertTrue(mySpring.set_dampfactor(dampfactor))
        self.assertEqual(mySpring.get_dampfactor(), dampfactor)

        # # Set deadband length and read it from the robot
        self.assertTrue(mySpring.set_deadband(deadband))
        self.assertEqual(mySpring.get_deadband(), deadband)

        # # Set spring direction and read it from the robot
        self.assertTrue(mySpring.set_direction(direction))
        self.assertEqual(mySpring.get_direction(), direction)

        # # Set spring's maximum force and read it from the robot
        self.assertTrue(mySpring.set_maxforce(deadband))
        self.assertEqual(mySpring.get_maxforce(), deadband)

        # Set spring's global damping and read it from the robot
        self.assertTrue(mySpring.set_dampglobal(True))
        self.assertTrue(mySpring.get_dampglobal())

        # Remove effect
        self.assertTrue(mySpring.remove())

        robot.disconnect()

    def test_damper(self):
        '''
        Testing the damper effect
        '''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Create a damper instance
        myDamper = Damper(name='myDamper', robot=robot)

        # Create the damper on the HapticMaster controller
        self.assertTrue(myDamper.create())

        dampcoef = [0.2, 0.43, 0.59]

        # Set the damper's damping coefficient and read it from the robot
        self.assertTrue(myDamper.set_dampcoef(dampcoef))
        self.assertEqual(myDamper.get_dampcoef(), dampcoef)

        robot.disconnect()

    def test_bias_force(self):
        '''
        Testing the bias force effect
        '''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Create a damper instance
        myBiasForce = BiasForce(name='myBiasForce', robot=robot)

        # Create the damper on the HapticMaster controller
        self.assertTrue(myBiasForce.create())

        force = [0.192, 0.233, 0.995]

        # Set the bias force's value and read it from the robot
        self.assertTrue(myBiasForce.set_force(force))
        self.assertEqual(myBiasForce.get_force(), force)

        robot.disconnect()


if __name__ == '__main__':
    unittest.main()
