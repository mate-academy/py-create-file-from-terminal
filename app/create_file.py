import argparse
import sys

print("glob")
def parsefunc():
    parser = argparse.ArgumentParser()
    print(sys.argv)
    print(parser)
    print("func")

if __name__ == '__main__':
    parsefunc()