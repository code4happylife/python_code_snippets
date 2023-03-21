import unittest
import HtmlTestRunner

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2+2, 4)
    
    def test_subtraction(self):
        self.assertEqual(5-3, 2)
    
    def test_multiplication(self):
        self.assertEqual(3*4, 12)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
