import unittest
from randomgame import check_answer


class TestCheckAnswer(unittest.TestCase):
    def setUp(self) -> None:
        self.target = 5

    def test_right_answer(self):
        answer = 5
        result = check_answer(answer, self.target)
        self.assertTrue(result)

    def test_wrong_answer(self):
        answer = 7
        result = check_answer(answer, self.target)
        self.assertFalse(result)

    def test_num_out_of_range(self):
        answer = 20
        result = check_answer(answer, self.target)
        self.assertFalse(result)
