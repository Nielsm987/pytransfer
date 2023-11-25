from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "service_account.json"
PARENT_FOLDER_ID = "1K5Z9OwLBF-DhMjSLUAKSpgeWbtVPWJFY"

file_name = input("Enter filename: ")


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

    return share_link


shareable_link = upload("invoice.pdf")
print("Shareable link:", shareable_link)
