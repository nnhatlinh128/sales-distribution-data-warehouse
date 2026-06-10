import pandas as pd


def parse_file(file_path):

    file_path = file_path.lower()

    # CSV
    if file_path.endswith(".csv"):

        df = pd.read_csv(
            file_path,
            encoding="utf-8-sig"
        )

    # XLSX
    elif file_path.endswith(".xlsx"):

        df = pd.read_excel(
            file_path,
            engine="openpyxl"
        )

    # XLSM
    elif file_path.endswith(".xlsm"):

        df = pd.read_excel(
            file_path,
            engine="openpyxl"
        )

    # XLSB
    elif file_path.endswith(".xlsb"):

        df = pd.read_excel(
            file_path,
            engine="pyxlsb"
        )

    else:
        raise ValueError(
            f"Unsupported file format: {file_path}"
        )

    return df