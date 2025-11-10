"""Combine all CSV files in a directory into a single CSV."""
import os
import pandas as pd


def combine_csv_files(directory: str, output_file: str = "combined.csv"):
    all_data = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(".csv"):
            path = os.path.join(directory, filename)
            df = pd.read_csv(path)
            all_data.append(df)
    if not all_data:
        return
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False)


if __name__ == "__main__":
    combine_csv_files("<directory>", "Combined.csv")
