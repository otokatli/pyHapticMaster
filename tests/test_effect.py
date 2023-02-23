import unittest
from haptic_master.haptic_master import HapticMaster
from haptic_master.effect import BiasForce, Damper, Spring


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
        my_spring = Spring(name='mySpring', robot=robot)

        # Create the spring on the HapticMaster controller
        self.assertTrue(my_spring.create())

        # Set position of the spring and read it from the robot
        self.assertTrue(my_spring.set_pos(position))
        self.assertEqual(my_spring.get_pos(), position)

        # Set velocity of the spring and read it from the robot
        self.assertTrue(my_spring.set_vel(velocity))
        self.assertEqual(my_spring.get_vel(), velocity)

        # Set attitude of the spring and read it from the robot
        self.assertTrue(my_spring.set_att(attitude))
        # self.assertAlmostEqual(my_spring.get_att(), attitude, places=5)

        # Enable the spring
        self.assertTrue(my_spring.set_enable())
        self.assertEqual(my_spring.get_enabled(), True)

        # Disable the spring
        self.assertTrue(my_spring.set_disable())
        self.assertEqual(my_spring.get_enabled(), False)

        # Set stiffness and read it from the robot
        self.assertTrue(my_spring.set_stiffness(stiffness))
        self.assertEqual(my_spring.get_stiffness(), stiffness)

        # # Set damping factor and read it from the robot
        self.assertTrue(my_spring.set_dampfactor(dampfactor))
        self.assertEqual(my_spring.get_dampfactor(), dampfactor)

        # # Set deadband length and read it from the robot
        self.assertTrue(my_spring.set_deadband(deadband))
        self.assertEqual(my_spring.get_deadband(), deadband)

        # # Set spring direction and read it from the robot
        self.assertTrue(my_spring.set_direction(direction))
        self.assertEqual(my_spring.get_direction(), direction)

        # # Set spring's maximum force and read it from the robot
        self.assertTrue(my_spring.set_maxforce(deadband))
        self.assertEqual(my_spring.get_maxforce(), deadband)

        # Set spring's global damping and read it from the robot
        self.assertTrue(my_spring.set_dampglobal(True))
        self.assertTrue(my_spring.get_dampglobal())

        # Remove effect
        self.assertTrue(my_spring.remove())

        robot.disconnect()

    def test_damper(self):
        '''
        Testing the damper effect
        '''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Create a damper instance
        my_damper = Damper(name='myDamper', robot=robot)

        # Create the damper on the HapticMaster controller
        self.assertTrue(my_damper.create())

        dampcoef = [0.2, 0.43, 0.59]

        # Set the damper's damping coefficient and read it from the robot
        self.assertTrue(my_damper.set_dampcoef(dampcoef))
        self.assertEqual(my_damper.get_dampcoef(), dampcoef)

        robot.disconnect()

    def test_bias_force(self):
        '''
        Testing the bias force effect
        '''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Create a damper instance
        my_bias_force = BiasForce(name='myBiasForce', robot=robot)

        # Create the damper on the HapticMaster controller
        self.assertTrue(my_bias_force.create())

        force = [0.192, 0.233, 0.995]

        # Set the bias force's value and read it from the robot
        self.assertTrue(my_bias_force.set_force(force))
        self.assertEqual(my_bias_force.get_force(), force)

        robot.disconnect()


if __name__ == '__main__':
    unittest.main()
