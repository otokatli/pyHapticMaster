from haptic_master.haptic_master import HapticMaster
from haptic_master.effect import Spring
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_state(self):
        print('Testing states')
        
        # Open connection and set inertia to 1.0
        robot = HapticMaster(IP, PORT, 1.0)
        robot.connect()

        # Set state to position
        print('Setting state to position')
        response = robot.set_state('position')
        self.assertEqual(response, 'INFO: \x00\x00\x00\x19\x00\x00\x00\x00state set to \'position\'')

        # Set state to force
        print('Setting state to force')
        response = robot.set_state('force')
        self.assertEqual(response, 'INFO: \x00\x00\x00\x16\x00\x00\x00\x00state set to \'force\'')

        robot.disconnect()

    def test_spring(self):
        print('Testing spring')

        # Open connection and set inertia to 1.0
        robot = HapticMaster(IP, PORT, 1.0)
        robot.connect()

        # Create spring object
        mySpring = Spring(name='mySpring', position=[0.0, 0.0, 0.0], velocity=[0.0, 0.0, 0.0], attitude=[0.0, 0.0, 0.0, 1.0], stiffness=100, dampfactor=0.0, deadband=0.0, direction=[0.0, 0.0, 1.0], maxforce=25.0, dampglobal=False)

        print('Creating the spring')
        self.assertTrue(robot.create_spring(mySpring))

        print('Move the spring')
        self.assertTrue(robot.move_spring(mySpring, [0.0, 0.0, 0.1]))

        robot.disconnect()

    # def test_damper(self):
    #     print('Testing damper')

    #     # Open connection and set inertia to 1.0
    #     robot = HapticMaster(IP, PORT, 1.0)
    #     robot.connect()

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