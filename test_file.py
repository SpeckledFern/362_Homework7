import unittest
import programs

class TestPrograms(unittest.TestCase):
   def test_output(self):
      self.assertEqual(programs.output_at(5), "Buzz")
      self.assertEqual(programs.output_at(6), "Fizz")
      self.assertEqual(programs.output_at(30), "FizzBuzz")
      self.assertEqual(programs.list_print(), 100)
   def test_leap(self):
      self.assertEqual(programs.leap(4), "true")
      self.assertEqual(programs.leap(5), "false")
      self.assertEqual(programs.leap(8), "true")
      self.assertEqual(programs.leap(2000), "true")


if __name__ == "__main__":
   unittest.main()
