from ingestion.connectors.gdrive_connector import (
    list_files_in_folder
)

FOLDER_ID = "1DxPEHsw8n8_jv6KKSgEdAoEpbkqSWGaa"

files = list_files_in_folder(FOLDER_ID)

print(files)