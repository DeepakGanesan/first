""" This is my first code in pycharm. I shall be setting up a package that can be run from the command line.
This shall also include logging functions and will be linked to a remote repo."""

import argparse
import preprocess.analyze as ace

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze any pandas dataframe")
    parser.add_argument("-x", "--xvar", type=int, help="1 for analyzing")
    args = parser.parse_args()
    if args.xvar == 1:
        analyzer = ace.Analyze("./data/example.csv")
        analyzer.column_sum()
