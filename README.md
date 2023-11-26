### Configuration Setup

1. **Configuration File:**

   - Duplicate `example_config.py` as `config.py`.
   - Replace placeholder values in `config.py` with your actual credentials and IDs.

2. **Google Drive API Credentials:**

   - Obtain the service account JSON file from the Google Cloud Console.
   - Update the `SERVICE_ACCOUNT_FILE` path in `config.py` with the downloaded file's path.

3. **Google Drive Parent Folder ID:**
   - Replace the `PARENT_FOLDER_ID` value in `config.py` with the desired Google Drive folder ID found in the URL when you are inside the folder.
