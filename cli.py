import argparse
import yaml

with open(r"first\configs\input.yaml", "rb") as f:
    config = yaml.safe_load(f)

import first.preprocess.analyze as ace


def cli():
    parser = argparse.ArgumentParser(description="Analyze any pandas dataframe")
    parser.add_argument("-x", "--xvar", type=int, help="1 for analyzing")
    args = parser.parse_args()
    if args.xvar == 1:
        analyzer = ace.Analyze(config['data']['input'])
        analyzer.column_sum()
