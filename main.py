""" This is my first code in pycharm. I shall be setting up a package that can be run from the command line.
This shall also include logging functions and will be linked to a remote repo."""

import preprocess.analyze as ace

if __name__ == "__main__":
    analyzer = ace.Analyze("./data/example.csv")
    analyzer.column_sum()
