"""
This module covers the logging module that creates a logger object
"""
import logging


class Customlogger:

    def __init__(self, name: str, path: str):

        # Create a logger object
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Create a stream handler
        self.sh = logging.StreamHandler()
        # Create a filehandler
        self.fh = logging.FileHandler(path, mode='w')

    def create_log(self):

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s  - %(message)s')

        self.sh.setLevel(logging.DEBUG)
        self.fh.setLevel(logging.DEBUG)

        # add formatter to ch
        self.sh.setFormatter(formatter)
        self.fh.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)

        return self.logger
