"""
An analyze class that will analyze the input pandas dataframe multiple ways
"""
import pandas as pd


class Analyze:

    def __init__(self,path: str):
        self.example = pd.read_csv(path)
        print(self.example.head(), "\n", self.example.shape)

    def column_sum(self) -> None:
        """Prints an array or data series

        Args:
            takes in a single pandas dataframe parameter
        """

        print(self.example.sum(axis=1))
        print(type(self.example.sum(axis=1)))
