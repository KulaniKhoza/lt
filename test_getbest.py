import getbest
import unittest
from io import StringIO
class TestingGetBest(unittest.Testcase):

def setUp(self):
self.data = [
            ["ELEN3020", "StudentNumber", "Mark", "Comment"],
            ["ELEN3020", "160001", "72", "OK"],
            ["ELEN3020", "167381", "90", "Check"],
            ["ELEN3020", "143211", "83", "-"]
        ]
def test_getCols(self):
num_col, mark_col = getbest.getCols(self.data[0])
self.assertEqual(num_col, 0)
self.assertEqual(mark_col, 2))

if __name__ == '__main__':
unittest.main()
