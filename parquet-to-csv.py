#!/usr/bin/python

import pandas as pd
import sys

[parquet_source, csv_destination] = sys.argv[1:]

print("Loading dataframe from Parquet file:", parquet_source)
df = pd.read_parquet(parquet_source)

print("Saving dataframe to CSV:", csv_destination)
df.to_csv(csv_destination)
