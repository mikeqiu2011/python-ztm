import unittest
from main import do_stuff


class TestMain(unittest.TestCase):
    def test_do_studff(self):
        num = 10
        result = do_stuff(num)
        self.assertEqual(15, result)


unittest.main()
