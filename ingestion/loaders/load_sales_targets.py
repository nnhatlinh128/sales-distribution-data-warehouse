import glob
import os
import uuid

from datetime import datetime

import pandas as pd

from ingestion.utils.db_utils import load_to_bronze


TABLE_NAME = "sales_targets_raw"


def run():

    batch_id = str(uuid.uuid4())

    files = glob.glob("data/raw/SRC02_sales_target_plan.xlsx")

    print(f"Found {len(files)} file(s)")

    for file_path in files:

        print(f"Processing file: {file_path}")

        excel_data = pd.read_excel(file_path, sheet_name=None, engine="openpyxl")

        for sheet_name, df in excel_data.items():

            if "Summary" in sheet_name:
                continue

            print(f"Processing sheet: {sheet_name}")

            df = df[df["employee_name"] != "TỔNG"]

            df["_source_file"] = (os.path.basename(file_path))

            df["_ingested_at"] = datetime.now()

            df["_batch_id"] = batch_id

            df["version_label"] = sheet_name

            rows = load_to_bronze(df, TABLE_NAME, if_exists="append")

            print(f"Loaded {rows} rows")

            version_df = pd.DataFrame([{
                "version_label": sheet_name,
                "source_file": os.path.basename(file_path),
                "loaded_at": datetime.now(),
                "batch_id": batch_id
            }])

            load_to_bronze( version_df, "sales_target_files", if_exists="append")

            print("Loaded version metadata")


if __name__ == "__main__":
    run()