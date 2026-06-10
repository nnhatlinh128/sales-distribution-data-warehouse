import glob
import os
import time
import uuid

from sqlalchemy import text

from ingestion.utils.file_parser import parse_file
from ingestion.utils.db_utils import (
    add_metadata,
    get_engine,
    load_to_bronze
)

TABLE_NAME = "sales_transactions"


def run():

    batch_id = str(uuid.uuid4())

    start = time.time()

    engine = get_engine()

    files = glob.glob("data/raw/SRC01_sales_transactions.csv")

    print(f"Found {len(files)} files")

    total_loaded = 0

    for file_path in files:

        try:

            df = parse_file(file_path)

            df = add_metadata(
                df,
                source_file=os.path.basename(file_path),
                source_platform="local",
                batch_id=batch_id
            )

            rows = load_to_bronze(
                df,
                TABLE_NAME,
                if_exists="append"
            )

            total_loaded += rows

            print(f"OK: {file_path} - {rows} rows")

            with engine.begin() as conn:

                conn.execute(text(
                    """
                    INSERT INTO raw.ingest_log
                    (
                        batch_id,
                        source_name,
                        source_file,
                        source_platform,
                        rows_loaded,
                        status,
                        duration_sec
                    )
                    VALUES
                    (
                        :bid,
                        :sn,
                        :sf,
                        :sp,
                        :rl,
                        :st,
                        :dur
                    )
                    """
                ), dict(
                    bid=batch_id,
                    sn=TABLE_NAME,
                    sf=os.path.basename(file_path),
                    sp="local",
                    rl=rows,
                    st="SUCCESS",
                    dur=round(time.time() - start, 2)
                ))

        except Exception as e:

            print(e)

    print(f"Total loaded: {total_loaded}")


if __name__ == "__main__":
    run()