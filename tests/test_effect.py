from haptic_master.haptic_master import HapticMaster
from haptic_master.effect import Spring
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_state(self):
        '''
        Testing the robot communication and setting the robot states to
        position and force
        '''
        
        # Open connection 
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # End-effector inertia value for the robot
        end_effector_inertia = 2.3

        # Set the inertia
        robot.set_inertia(end_effector_inertia)

        # Get inertia value
        self.assertEqual(robot.get_inertia(), end_effector_inertia)

        # Set state to position
        self.assertEqual(robot.set_state('position'), 'state set to \'position\'')

        # Set state to force
        self.assertEqual(robot.set_state('force'), 'state set to \'force\'')

        robot.disconnect()

    def test_spring(self):
        # print('Testing spring')

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Create spring object
        stiffness = 10.0
        dampfactor = 0.01
        deadband = 0.023
        direction = [1.0, 0.0, 0.0]
        maxforce = 24.2
        dampglobal = False

        # Create a spring instance
        mySpring = Spring(name='mySpring', robot=robot)

        # Create the spring on the HapticMaster controlelr
        self.assertTrue(mySpring.create())

        # Set stiffness
        self.assertTrue(mySpring.set_stiffness(stiffness))
        
        # Check stiffness value
        self.assertEqual(mySpring.get_stiffness(), stiffness)

    #     # Set damping factor
    #     self.assertTrue(mySpring.set_dampfactor(dampfactor))
    #     self.assertEqual(mySpring.get_dampfactor(), dampfactor)

    #     # Set deadband length
    #     self.assertTrue(mySpring.set_deadband(deadband))
    #     self.assertEqual(mySpring.get_deadband(), deadband)

    #     # Set spring direction

    #     # Set spring's maximum force
    #     self.assertTrue(mySpring.set_maxforce(deadband))
    #     self.assertEqual(mySpring.get_maxforce(), deadband)

    #     # Set spring's global damping


        robot.disconnect()

    # def test_damper(self):
    #     print('Testing damper')

    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     # Create spring object
    #     mySpring = Damper(name='myDamper')

    #     # print('Creating the spring')
    #     # self.assertTrue(robot.(mySpring))

    #     print('Checking if the spring is enabled')
    #     self.assertTrue(robot.is_enabled(mySpring.name))

    #     print('Move the spring')
    #     self.assertTrue(robot.set_position(mySpring, [0.0, 0.0, 0.1]))

    #     print('Disabling the spring')
    #     self.assertTrue(robot.disable(mySpring.name))

    #     print('Checking if the spring is disabled')
    #     self.assertFalse(robot.is_enabled(mySpring.name))

    #     robot.disconnect()

    # def test_bias_force(self):
    #     print('Testing bias force')

    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

    # def test_inertia(self):
    #     print('Testing inertia')
        
    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

    # def test_block(self):
    #     print('Testing block')
        
    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

    # def test_sphere(self):
    #     print('Testing sphere')
        
    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

    # def test_flat_plane(self):
    #     print('Testing flat plane')
        
    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

    # def test_cylinder(self):
    #     print('Testing cylinder')
        
    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

    # def test_torus(self):
    #     print('Testing torus')
        
    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

    # def test_shaker(self):
    #     print('Testing shaker')
        
    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     robot.disconnect()

        
if __name__ == '__main__':
    unittest.main()