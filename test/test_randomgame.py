import unittest
from randomgame import check_answer


class TestCheckAnswer(unittest.TestCase):
    def setUp(self) -> None:
        self.target = 5

    def test_right_answer(self):
        answer = 5
        result = check_answer(answer, self.target)
        self.assertTrue(result)
