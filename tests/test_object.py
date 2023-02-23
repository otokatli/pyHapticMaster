from haptic_master.haptic_master import HapticMaster
from haptic_master.object import Block, Cylinder, FlatPlane, Sphere, Torus
import unittest


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    def test_block(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        myBlock = Block('myBlock', robot)

        self.assertTrue(myBlock.create())

        stiffness = 10.23
        dampfactor = 0.593
        no_pull = False
        tang_damping = 0.0432
        damping_forcemax = 1.203
        friction = 2.302
        ejection_velmax = 0.232
        ejection_damping = 0.392
        outward_forcemax = 20.23
        powermax = 102.0
        block_size = [0.23, 0.31, 0.15]

        # Set the stiffness of the object and read it from the robot
        self.assertTrue(myBlock.set_stiffness(stiffness))
        self.assertEqual(myBlock.get_stiffness(), stiffness)

        # Set damping factor of the object and read it from the robot
        self.assertTrue(myBlock.set_dampfactor(dampfactor))
        self.assertEqual(myBlock.get_dampfactor(), dampfactor)

        # Set no pull of the object and read it from the robot
        self.assertTrue(myBlock.set_no_pull(no_pull))
        self.assertEqual(myBlock.get_no_pull(), no_pull)

        # Set tangential damping of the object and read it from the robot
        self.assertTrue(myBlock.set_tang_damping(tang_damping))
        self.assertEqual(myBlock.get_tang_damping(), tang_damping)

        # Set max damping force of the object and read it from the robot
        self.assertTrue(myBlock.set_damping_forcemax(damping_forcemax))
        self.assertEqual(myBlock.get_damping_forcemax(), damping_forcemax)

        # Set friction of the object and read it from the robot
        self.assertTrue(myBlock.set_friction(friction))
        self.assertEqual(myBlock.get_friction(), friction)

        # Set max ejection velocity of the object and read it from the robot
        self.assertTrue(myBlock.set_ejection_velmax(ejection_velmax))
        self.assertEqual(myBlock.get_ejection_velmax(), ejection_velmax)
        
        # Set ejection damping of the object and read it from the robot
        self.assertTrue(myBlock.set_ejection_damping(ejection_damping))
        self.assertEqual(myBlock.get_ejection_damping(), ejection_damping)

        # Set max outward force of the object and read it from the robot
        self.assertTrue(myBlock.set_outward_forcemax(outward_forcemax))
        self.assertEqual(myBlock.get_outward_forcemax(), outward_forcemax)

        # Set max power of the object and read it from the robot
        self.assertTrue(myBlock.set_powermax(powermax))
        self.assertEqual(myBlock.get_powermax(), powermax)

        # Set block size and read it from the robot
        self.assertTrue(myBlock.set_size(block_size))
        self.assertEqual(myBlock.get_size(), block_size)

        robot.disconnect()

    def test_sphere(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        mySphere = Sphere('mySphere', robot)

        self.assertTrue(mySphere.create())

        sphere_radius = 0.258

        self.assertTrue(mySphere.set_radius(sphere_radius))
        self.assertEqual(mySphere.get_radius(), sphere_radius)

        robot.disconnect()

    def test_flat_plane(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        myFlatPlane = FlatPlane('myFlatPlane', robot)

        self.assertTrue(myFlatPlane.create())

        plane_normal = [1.0, 0.0, 0.0]

        self.assertTrue(myFlatPlane.set_normal(plane_normal))
        self.assertEqual(myFlatPlane.get_normal(), plane_normal)

        robot.disconnect()

    def test_cylinder(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        myCylinder = Cylinder('myCylinder', robot)

        self.assertTrue(myCylinder.create())

        cylinder_radius = 0.201
        cylinder_length = 0.492

        self.assertTrue(myCylinder.set_radius(cylinder_radius))
        self.assertEqual(myCylinder.get_radius(), cylinder_radius)
        self.assertTrue(myCylinder.set_length(cylinder_length))
        self.assertEqual(myCylinder.get_length(), cylinder_length)

        robot.disconnect()

    def test_torus(self):
        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        myTorus = Torus('myTorus', robot)

        self.assertTrue(myTorus.create())

        torus_ring_radius = 0.203
        torus_outer_radius = 0.943

        self.assertTrue(myTorus.set_ringradius(torus_ring_radius))
        self.assertEqual(myTorus.get_ringradius(), torus_ring_radius)

        self.assertTrue(myTorus.set_tuberadius(torus_outer_radius))
        self.assertEqual(myTorus.get_tuberadius(), torus_outer_radius)

        robot.disconnect()

        
if __name__ == '__main__':
    unittest.main()