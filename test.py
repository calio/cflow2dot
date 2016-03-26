import unittest
from cflow2dot import *

class TestCflow2Dot(unittest.TestCase):

    def test_call_cflow(self):
        res = call_cflow(["a.c"])
        self.assertEqual("{   0} main() <int main (int argc, char **argv) at a.c:8>:\n{   1}     foo() <int foo () at a.c:3>\n", res)

if __name__ == '__main__':
    unittest.main()
