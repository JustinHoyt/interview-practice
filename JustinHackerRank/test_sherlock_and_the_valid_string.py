import unittest
from sherlock_and_the_valid_string import valid_string

class TestStringMethods(unittest.TestCase):

  def test_same_number_of_occurances(self):
      validate = valid_string()
      self.assertEqual(validate.is_valid("aabbcc"), "YES")

  def test_off_by_one_number_of_occurances(self):
      validate = valid_string()
      self.assertEqual(validate.is_valid("aabbc"), "YES")

  def test_off_by_one_number_of_occurances_twice(self):
      validate = valid_string()
      self.assertEqual(validate.is_valid("aabbcd"), "NO")

if __name__ == '__main__':
    unittest.main()
