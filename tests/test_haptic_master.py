from haptic_master.haptic_master import HapticMaster
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_connection(self):
        '''
        Testing the robot communication
        '''
        
        # Open connection 
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()
    
    def test_state(self):
        '''
        Testing the robot states, set the robot states to position and force
        '''
        
        # Open connection 
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Set state to position
        self.assertEqual(robot.set_state('position'), 'state set to \'position\'')

        # Set state to force
        self.assertEqual(robot.set_state('force'), 'state set to \'force\'')

        robot.disconnect()

    def test_inertia(self):
        '''
        Testing the inertia of the robot, set the inertia to the specified
        value and read the inertia from the robot
        '''
            
        # Open connection]
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # End-effector inertia value for the robot
        end_effector_inertia = 2.3

        # Set the inertia
        robot.set_inertia(end_effector_inertia)

        # Get inertia value
        self.assertEqual(robot.get_inertia(), end_effector_inertia)

        robot.disconnect()


if __name__ == '__main__':
    unittest.main()