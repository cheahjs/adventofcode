#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
