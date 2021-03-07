import unittest
import programs

class TestPrograms(unittest.TestCase):
   def test_output(self):
      self.assertEqual(programs.output_at(5), "Buzz")
      self.assertEqual(programs.output_at(6), "Fizz")


if __name__ == "__main__":
   unittest.main()
