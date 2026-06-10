from ingestion.utils.file_parser import parse_file

df = parse_file("data/raw/SRC05_distributor_orders.xlsx")

print(df.head())
print(df.shape)
print(df.columns)