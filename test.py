import unittest
import argparse
from cflow2dot import *

class TestCflow2Dot(unittest.TestCase):

    def test_call_cflow(self):
        res = call_cflow(["tests/a.c"])
        self.assertEqual("{   0} main() <int main (int argc, char **argv) at tests/a.c:8>:\n{   1}     foo() <int foo () at tests/a.c:3>\n", res)

    def test_get_output(self):
        ap = get_parser()
        opts = ap.parse_args(["tests/a.c"])
        flow = call_cflow(opts.cflow_args)
        res = get_output(opts, flow)
        self.assertEqual(['digraph G {\nnode [peripheries=2 style="filled,rounded" fontname="Vera Sans YuanTi Mono" color="#eecc80"];\nrankdir=LR;\nlabel="tests/a.c"\n', 'main [shape=box];\n', 'node [color="#ccee80" shape=ellipse];edge [color="#ccee80"];\nmain->foo\n', '}\n'], res)

if __name__ == '__main__':
    unittest.main()
