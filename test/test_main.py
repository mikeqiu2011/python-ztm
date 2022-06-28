import unittest
from main import do_stuff


class TestDoStuff(unittest.TestCase):
    def setUp(self) -> None:
        print('about to test a function')

    def test_normal(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_string(self):
        test_param = 'sasas'
        result = do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_none(self):
        '''
        To test input of None
        '''
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, 5)

    def test_empty_string(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 5)

    def test_default(self):
        result = do_stuff()
        self.assertEqual(result, 5)

    def tearDown(self) -> None:
        print('clear things up')

# if __name__ == '__main__':
#     unittest.main()
