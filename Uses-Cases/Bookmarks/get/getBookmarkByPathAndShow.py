import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, BookmarkResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    BOOKMARK_PATH = "/5"

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
                api_key, app_id = credentials.get("key"), credentials.get("id")
                if not api_key or not app_id:
                    raise ValueError("Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"Failed to load credentials: {e}")

    def _ensure_api_initialized(self):
        """Check if the API is initialized before making API calls."""
        if not self.pdf_api:
            logging.error("PDF API is not initialized. Operation aborted.")
            return False
        return True

    def upload_document(self):
        """Upload a PDF document to the Aspose Cloud server."""
        if not self._ensure_api_initialized():
            return

        file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
        try:
            self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
            logging.info(f"File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
        except Exception as e:
            logging.error(f"Failed to upload file: {e}")

    def get_bookmark(self):
        """Get bookmark for a specific PDF document using bookmark path."""    
        if not self._ensure_api_initialized():
            return

        try:
            response : BookmarkResponse = self.pdf_api.get_bookmark( Config.PDF_DOCUMENT_NAME, Config.BOOKMARK_PATH)
            if response.code == 200:
                logging.info(f"Found bookmark => level: '{response.bookmark.level}' - action: '{response.bookmark.action}' - title: '{response.bookmark.title}'")
            else:
                logging.error(f"Failed to find bookmark for the document. Response code: {response.code}")
        except Exception as e:
            logging.error(f"Error while find bookmark: {e}")

if __name__ == "__main__":
    pdf_bookmarks = PdfBookmarks()
    pdf_bookmarks.upload_document()
    pdf_bookmarks.get_bookmark()