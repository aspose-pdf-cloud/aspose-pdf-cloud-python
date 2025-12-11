import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, AsposeResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "PdfWithBookmarks.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    BOOKMARK_PATH = "/1"


class PdfBookmarks:
    """Class for managing PDF bookmarks using Aspose PDF Cloud API."""

    def __init__(self, credentials_file: Path = Config.CREDENTIALS_FILE):
        self.pdf_api = None
        self._init_api(credentials_file)

    def _init_api(self, credentials_file: Path):
        """Initialize the API client."""
        try:
            with credentials_file.open("r", encoding="utf-8") as file:
                credentials = json.load(file)
                api_key, app_id = credentials.get("client_secret"), credentials.get("client_id")
                if not api_key or not app_id:
                    raise ValueError("Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"Failed to load credentials: {e}")

    def upload_document(self):
        """Upload a PDF document to the Aspose Cloud server."""
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"Failed to upload file: {e}")

    def download_result(self):
        """Download the processed PDF document from the Aspose Cloud server."""
        if self.pdf_api:
            try:
                temp_file = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
                local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def remove_bookmark_by_path(self):
        if self.pdf_api:
            response: AsposeResponse = self.pdf_api.delete_bookmark(Config.PDF_DOCUMENT_NAME, Config.BOOKMARK_PATH)

            if response.code == 200:
                logging.info(f"Bookmark with path: '{Config.BOOKMARK_PATH}' has been removed.")
            else:
                logging.erro(f"Failed to remove bookmark with path: '{Config.LINK_FIND_ID}")

if __name__ == "__main__":
    pdf_bookmarks = PdfBookmarks()
    pdf_bookmarks.upload_document()
    pdf_bookmarks.remove_bookmark_by_path()
    pdf_bookmarks.download_result()
