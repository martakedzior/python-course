import unittest
from fields import rectangle

class FieldsTestCase(unittest.TestCase):
  def setUp(self):
    self.a = 2
    self.b = 10

  def test_rectangle_with_correct_values(self):
    result = rectangle(self.a, self.b)
    self.assertEqual(result, 20)


if __name__ == "main":
  unittest.main()