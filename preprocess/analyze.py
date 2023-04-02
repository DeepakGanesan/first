"""
An analyze class that will analyze the input pandas dataframe multiple ways
"""
import pandas as pd


class Analyze:

    def __init__(self, path: str, logobject):
        self.example = pd.read_csv(path)
        self.logger = logobject
        print(self.example.head(), "\n", self.example.shape)

    def column_sum(self) -> None:
        """Prints an array or data series

        Args:
            takes in a single pandas dataframe parameter
        """
        self.logger.info("Performing column sum operation")
        print(self.example.sum(axis=1))
        print(type(self.example.sum(axis=1)))
