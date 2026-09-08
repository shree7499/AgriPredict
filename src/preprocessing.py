import pandas as pd


def load_data(file_path):
    """Load mandi price data."""
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """Basic data cleaning."""
    df = df.copy()

    df["data"] = pd.to_datetime(df["data"])

    df = df.drop_duplicates()

    df = df.sort_values(["market", "date"])

    return df


if __name__ == "__main__":
    print("AgriPredict preprocessing module")