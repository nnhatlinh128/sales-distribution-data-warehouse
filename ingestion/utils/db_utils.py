import os
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def get_engine():

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    connection_string = (
            f"postgresql://{db_user}"
            f"@{db_host}:{db_port}/{db_name}"
        )

    engine = create_engine(connection_string)

    return engine


def add_metadata(
    df,
    source_file,
    source_platform,
    batch_id
):

    df["_source_file"] = source_file

    df["_source_platform"] = source_platform

    df["_ingested_at"] = datetime.now()

    df["_batch_id"] = batch_id

    return df


def load_to_bronze(
    df,
    table_name,
    if_exists="append"
):

    engine = get_engine()

    # convert all columns to TEXT
    df = df.astype(str)

    df.to_sql(
        name=table_name,
        con=engine,
        schema="raw",
        if_exists=if_exists,
        index=False
    )

    return len(df)