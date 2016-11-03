#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    print "Usage:", sys.argv[0], "FILENAME"
else:
    for f in file(sys.argv[1]).read():
        print ord(f),
