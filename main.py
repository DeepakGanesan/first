""" This is my first code in pycharm. I shall be setting up a package that can be run from the command line.
This shall also include logging functions and will be linked to a remote repo."""
import pandas as pd

example = pd.read_csv("example.csv")

print(example.head(), "\n", example.shape)


def column_sum(input_df: pd.DataFrame) -> None:
    """Prints an array or data series

    Args:
        takes in a single pandas dataframe parameter
    """

    print(input_df.sum(axis=1))
    print(type(input_df.sum(axis=1)))


if __name__ == "__main__":
    column_sum(example)
