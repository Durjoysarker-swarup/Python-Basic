import sys

from Library import hello
#find the file and read from top to bottom and then give the specific. 


if len(sys.argv) == 2:
    hello(sys.argv[1])
    