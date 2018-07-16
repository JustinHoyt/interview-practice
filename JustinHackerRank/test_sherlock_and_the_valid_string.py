import unittest
from sherlock_and_the_valid_string import valid_string

class TestStringMethods(unittest.TestCase):

  def test_same_number_of_occurances(self):
      validate = valid_string()
      self.assertEqual(validate.is_valid("aabbcc"), "YES")

  def test_two_chars_over_by_one(self):
      validate = valid_string()
      self.assertEqual(validate.is_valid("aabbc"), "YES")

  def test_off_by_one_number_of_occurances_twice(self):
      validate = valid_string()
      self.assertEqual(validate.is_valid("aabbcd"), "NO")

  def test_one_char_over_by_one_occurance(self):
      validate = valid_string()
      self.assertEqual(validate.is_valid("aabcd"), "YES")

if __name__ == '__main__':
    unittest.main()
