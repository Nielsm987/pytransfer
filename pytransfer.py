import os
import sys
import subprocess
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "service_account.json"
PARENT_FOLDER_ID = "1K5Z9OwLBF-DhMjSLUAKSpgeWbtVPWJFY"


def authenticate():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return creds


def upload(file_path):
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)

    file_metadata = {"name": file_name, "parents": [PARENT_FOLDER_ID]}
    media = MediaFileUpload(file_path)

    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )

    # Get the file ID
    file_id = file.get("id")

    # Generate the share link
    share_link = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"

    # Copy the shareable link to clipboard (macOS)
    subprocess.run(["pbcopy"], text=True, input=share_link.strip())

    return share_link


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
    else:
        file_name = sys.argv[1]
        home_folder = os.path.expanduser("~")
        found = False
        for root, dirs, files in os.walk(home_folder):
            if file_name in files:
                found = True
                file_path = os.path.join(root, file_name)
                shareable_link = upload(file_path)
                print("Shareable link:", shareable_link)
                print("Shareable link copied to clipboard.")
                break

        if not found:
            print("File not found in the home directory.")
