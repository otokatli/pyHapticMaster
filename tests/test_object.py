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

        block_size = [0.23, 0.31, 0.15]

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

    # def test_torus(self):
        # Open connection
        # robot = HapticMaster(IP, PORT)
        # robot.connect()

        # myTorus = Torus('myTorus', robot)

        # self.assertTrue(myTorus.create())

        # torus_ring_radius = 0.203
        # torus_outer_radius = 0.943

        # print(myTorus.set_ring_radius(torus_ring_radius))
        # print(myTorus.set_tube_radius(torus_outer_radius))

        # robot.disconnect()

        
if __name__ == '__main__':
    unittest.main()