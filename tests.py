import unittest
from main import Direction

class DirectionTestCase(unittest.TestCase):
  def test_enumeration(self):
    d = Direction.UP
    self.assertEqual(int(d), 0)
    d = d.clockwise()
    self.assertEqual(d, Direction.RIGHT)
    d = d.counterclockwise()
    self.assertEqual(d, Direction.UP)