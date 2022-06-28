import unittest
from main import do_stuff


class TestMain(unittest.TestCase):
    def test_do_stuff_input_normal(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_input_string(self):
        test_param = 'sasas'
        result = do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_input_none(self):
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, 5)

    def test_do_stuff_input_empty_string(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 5)

    def test_do_stuff_input_default(self):
        result = do_stuff()
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
