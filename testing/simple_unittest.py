import unittest 

class SimpleTest(unittest.TestCase): 

	def test(self):		 
		self.assertTrue(True) 

	# unittest will automatic find prefix with test_*
	# this function won't run
	def hello(self):
		self.assertFalse(False)

	# assertion e.g.
	# assertEqual
	# assertTrue
	# assertFalse
	# assertIs
	# assertIsNone
	# assertIn
	# assertIsInstance

	# .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot()

if __name__ == '__main__': 
	unittest.main() 
