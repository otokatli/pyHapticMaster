from haptic_master.haptic_master import HapticMaster
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_state(self):
        print('Testing states')
        
        # Open connection and set inertia to 1.0
        robot = HapticMaster(IP, PORT)
        robot.connect()

        end_effector_inertia = 2.3

        # Set the inertia
        print('Setting inertia of the robot')
        robot.set_inertia(end_effector_inertia)

        # Get inertia value
        self.assertEqual(robot.get_inertia(), end_effector_inertia)

        # Set state to position
        print('Setting state to position')
        self.assertEqual(robot.set_state('position'), 'state set to \'position\'')

        # Set state to force
        print('Setting state to force')
        self.assertEqual(robot.set_state('force'), 'state set to \'force\'')

        robot.disconnect()

    # def test_spring(self):
    #     print('Testing spring')

    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

    #     # Create spring object
    #     mySpring = Spring(name='mySpring')

    #     print('Creating the spring')
    #     self.assertTrue(robot.create_spring(mySpring))

    #     print('Checking if the spring is enabled')
    #     self.assertTrue(robot.is_enabled(mySpring.name))

    #     print('Move the spring')
    #     self.assertTrue(robot.move_spring(mySpring, [0.0, 0.0, 0.1]))

    #     print('Disabling the spring')
    #     self.assertTrue(robot.disable(mySpring.name))

    #     print('Checking if the spring is disabled')
    #     self.assertFalse(robot.is_enabled(mySpring.name))

    #     robot.disconnect()

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