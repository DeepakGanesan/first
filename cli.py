import argparse
import yaml

import first.preprocess.analyze as ace
from first.utilities.logger import Customlogger

with open(r"first\configs\input.yaml", "rb") as f:
    config = yaml.safe_load(f)

mylogger = Customlogger('__name__', config['data']['log'])
logger = mylogger.create_log()


def cli():
    parser = argparse.ArgumentParser(description="Analyze any pandas dataframe")
    parser.add_argument("-x", "--xvar", type=int, help="1 for analyzing")
    args = parser.parse_args()
    if args.xvar == 1:
        analyzer = ace.Analyze(config['data']['input'], logger)
        analyzer.column_sum()
        logger.info("Completed all operations")

