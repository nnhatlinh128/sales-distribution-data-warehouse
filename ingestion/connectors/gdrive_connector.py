import io
import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive"]

SERVICE_ACCOUNT_FILE = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT_JSON"
)

credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

drive_service = build(
    "drive",
    "v3",
    credentials=credentials
)


def list_files_in_folder(folder_id):

    query = f"'{folder_id}' in parents and trashed=false"

    results = drive_service.files().list(
        q=query,
        fields="files(id, name, mimeType)"
    ).execute()

    return results.get("files", [])


def download_file_as_bytes(file_id):

    request = drive_service.files().get_media(
        fileId=file_id
    )

    file_stream = io.BytesIO()

    downloader = MediaIoBaseDownload(
        file_stream,
        request
    )

    done = False

    while done is False:
        status, done = downloader.next_chunk()

    file_stream.seek(0)

    return file_stream.read()