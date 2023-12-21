import camelot.io as camelot
import pandas as pd

PDF_PATH = "/app/sauvieduckcounts.pdf"
CSV_PATH = "./foo.csv"
COLUMNS = [
    "Location",
    "Blind",
    "Hunters (Daily)",
    "Ducks (Daily)",
    "Geese (Daily)",
    "Ducks per Hunter (Daily)",
    "Hunters (Season)",
    "Ducks (Season)",
    "Geese (Season)",
    "Ducks per Hunter (Season)",
]
SHIFT_COL_IDX = 5
OUT_PATH = "./out_data/out.csv"


def split_newline_values(row):
    for col in df.columns:
        if "\n" in str(row[col]):
            new_values = row[col].split("\n")
            missing = COLUMNS[COLUMNS.index(col) :]
            idx = 0
            for miss in new_values:
                row[missing[idx]] = float(miss)
                idx += 1
            break
    return row


def shift_empty_values(row):
    if pd.isna(row.iloc[-1]):
        shifted_values = row.iloc[SHIFT_COL_IDX:].shift(1)
        return pd.concat([row.iloc[:SHIFT_COL_IDX], shifted_values])


tables = camelot.read_pdf(PDF_PATH, pages="2")
tables[0].to_csv(CSV_PATH)

df = pd.read_csv(CSV_PATH, names=COLUMNS)
df = df.iloc[2:]
df = df.dropna(how="all")
df["Location"] = df["Location"].fillna(method="ffill")
df["Location"] = df["Location"].str.replace("\n", "", regex=True)
for idx, row in df.iterrows():
    row = split_newline_values(row)
    df.loc[idx] = row
for idx, row in df.iterrows():
    row = shift_empty_values(row)
    if row is not None:
        df.loc[idx] = row

df.to_csv(OUT_PATH)
