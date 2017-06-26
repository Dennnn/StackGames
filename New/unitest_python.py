#!/usr/bin/python2.7
import unittest
from Game import *

class TestingClass(unittest.TestCase):

    #Test level 1
    def test_level_1(self):
        self.assertEqual(vecht(1,1,0,0,0,0,0,0), 0)
        self.assertEqual(vecht(1,1,0,100,100,0,0,0), 0)

    #Test level 2
    def test_level_2(self):
        self.assertNotEqual(vecht(2,1,1,100,100,0,0,0), 0)
        self.assertEqual(vecht(2,1,1,0,0,0,0,0), 0)

    #Test level 3
    def test_level_3(self):
        self.assertNotEqual(vecht(3,1,1,100,100,0,0,0), 0)
        self.assertEqual(vecht(3,1,1,20,20,0,0,0), 0)

    #Test pad 1
    def test_pad_1(self):
        self.assertNotEqual(vecht(1,1,1,100,100,0,0,0), 0)
        self.assertEqual(vecht(1,1,0,100,100,0,0,0), 0)

    #Test pad 2
    def test_pad_2(self):
        self.assertNotEqual(vecht(1,2,1,100,100,0,0,0), 0)
        self.assertEqual(vecht(1,2,0,5,5,0,0,0), 0)

    #Test pad 3
    def test_pad_3(self):
        self.assertNotEqual(vecht(1,3,1,100,100,0,0,0), 0)
        self.assertEqual(vecht(1,3,0,20,20,0,0,0), 0)

    #Test kopen wapens
    def test_koop_wapen(self):
        self.assertEqual(koop_of_verkoop(1,1,100), 50)

    #Testing for kooping schild
    def test_koop_schild(self):
        self.assertEqual(koop_of_verkoop(1,2,100), 40)

    #Testing for verkooping wapen
    def test_verkoop_wapen(self):
        self.assertEqual(koop_of_verkoop(2,1,100), 150)

    #Testing for verkooping schild
    def test_verkoop_schild(self):
        self.assertEqual(koop_of_verkoop(2,2,100), 160)



#Main Function
def main():
    unittest.main()

if __name__ == "__main__":
    main()


